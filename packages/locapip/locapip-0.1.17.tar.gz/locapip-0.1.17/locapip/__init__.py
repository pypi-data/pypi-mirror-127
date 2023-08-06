import asyncio
import importlib
import importlib.util
import json
import logging
import os
import sys
from pathlib import Path
from typing import Optional

import grpc
from google.protobuf.json_format import Parse, MessageToJson

sys.path.append(str(os.path.dirname(__file__)))
sys.path.append(str(Path(os.path.dirname(__file__)) / 'proto'))

name = 'locapip'
version = __version__ = '0.1.17'

server_port = 6547
config = {}
module = {}
server: Optional[grpc.aio.server] = None


def init_logging(filename: str):
    fmt = '[%(asctime)s]\t%(levelname)s\t%(message)s'
    logging.basicConfig(filename=filename, level=logging.INFO, format=fmt, datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('--------------------------------------------------')


def _import_module():
    for proto in config:
        if 'disable' in config[proto] and config[proto]['disable']:
            continue

        if 'path' in config[proto]:
            path = config[proto]['path']
        else:
            path = str(Path(os.path.dirname(__file__)) / 'proto' / (proto + '.py'))

        logging.info(f'import\t{path}')
        print(f'import\t{path}')

        spec = importlib.util.spec_from_file_location(proto, path)
        module[proto] = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module[proto])


def update_module(config_path):
    if Path(config_path).is_file():
        config.update(json.loads(Path(config_path).read_text()))


def reload_module():
    """
    only for client
    """
    if server is None:
        config.update({_: {} for _ in ['test', 'explorer', 'dicom', 'fit_fill']})
        _import_module()


async def _serve(port: int):
    global server, server_port
    if server is not None:
        await server.stop(None)
        logging.info(f'server\tstop {name} {version} [::]:{server_port}')
        print(f'server\tstop {name} {version} [::]:{server_port}')

    server = grpc.aio.server()
    server_port = port
    _import_module()

    server.add_insecure_port(f'[::]:{server_port}')
    await server.start()
    logging.info(f'server\tstart {name} {version} [::]:{server_port}')
    print(f'server\tstart {name} {version} [::]:{server_port}')


def serve(port: int, run_until_complete=True):
    asyncio.get_event_loop().run_until_complete(_serve(port))
    if run_until_complete:
        asyncio.get_event_loop().run_until_complete(server.wait_for_termination())


pb = {}
stub = {}
py_request = {}
py_response = {}


def _py_request_unary(request_type):
    async def foo(cpp_request_):
        return Parse(cpp_request_(str()), request_type())

    return foo


def _py_request_stream(request_type):
    async def foo(cpp_request_):
        while True:
            request_json_ = cpp_request_(str())
            if len(request_json_) == 0:
                break
            yield Parse(request_json_, request_type())

    return foo


async def _py_response_unary(response_message, cpp_response, *args):
    response_json = MessageToJson(response_message, True, True)
    cpp_response(response_json)


async def _py_response_stream(response_message_iterator, cpp_response, *args):
    async for response_message_ in response_message_iterator:
        cpp_response(MessageToJson(response_message_, True, True))
    cpp_response(str())


async def _run_rpc(url: str, proto: str, rpc: str, py_request_argv, py_response_argv):
    async with grpc.aio.insecure_channel(url) as channel:
        stub_ = getattr(stub[proto](channel), rpc)
        if 'UnaryUnary' in str(stub_.__class__):
            py_request_default = _py_request_unary
            py_response_default = _py_response_unary
        elif 'UnaryStream' in str(stub_.__class__):
            py_request_default = _py_request_unary
            py_response_default = _py_response_stream
        elif 'StreamUnary' in str(stub_.__class__):
            py_request_default = _py_request_stream
            py_response_default = _py_response_unary
        elif 'StreamStream' in str(stub_.__class__):
            py_request_default = _py_request_stream
            py_response_default = _py_response_stream

        if proto in py_request and rpc in py_request[proto]:
            if importlib.import_module(py_request[proto][rpc].__module__) is pb[proto]:
                py_request_ = py_request_default(py_request[proto][rpc])
            else:
                py_request_ = py_request[proto][rpc]
        else:
            raise NotImplementedError(f'{proto} {rpc} py_request not implemented')

        if proto in py_response and rpc in py_response[proto]:
            py_response_ = py_response[proto][rpc]
        else:
            py_response_ = py_response_default

        if type(py_request_argv) not in [list, tuple]:
            py_request_argv = [py_request_argv]

        if type(py_response_argv) not in [list, tuple]:
            py_response_argv = [py_response_argv]

        if 'UnaryUnary' in str(stub_.__class__):
            response_message = await stub_(await py_request_(*py_request_argv))
        elif 'UnaryStream' in str(stub_.__class__):
            response_message = stub_(await py_request_(*py_request_argv))
        elif 'StreamUnary' in str(stub_.__class__):
            response_message = await stub_(py_request_(*py_request_argv))
        elif 'StreamStream' in str(stub_.__class__):
            response_message = stub_(py_request_(*py_request_argv))
        await py_response_(response_message, *py_response_argv)


def run_rpc(url: str, proto: str, rpc: str, request, response):
    """
    async run rpc in proto on server at url, see specification in each proto.py

    :param url: server address
    :param proto: protocol buffer package
    :param rpc: remote procedure call
    :param request: vector<function<string<string>>> in py_request
    :param response: vector<function<string<string>>> in py_response
    """

    try:
        asyncio.get_event_loop().run_until_complete(_run_rpc(url, proto, rpc, request, response))
    except Exception as e:
        logging.exception(f'run @ url: {url} proto: {proto} rpc: {rpc}')
        raise e


def run_lpc(m: str, lpc: str, request):
    return getattr(module[m], lpc)(*request)
