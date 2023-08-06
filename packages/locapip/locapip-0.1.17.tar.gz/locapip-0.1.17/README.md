# C++嵌入式Python微服务

C++ embedded Python microservices

## 1 简介

locapip是一个小型gRPC运行框架，适用于内嵌Python解释器的C++项目。

结合locapic，可与虚幻引擎项目优雅集成

## 2 服务端

### 2.1 安装

```shell
python -m pip install locapip
```

### 2.2 启动

```shell
python -m locapip --port 6547 --config CONFIG_JSON
```

其中，```CONFIG_JSON```是配置文件的路径，定义启用的protobuf模块及其参数

```json
{
  "test": {},
  "fit_fill": {},
  "explorer": {
    "working_directory": "d:/"
  },
  "your_protobuf_module": {
    "path": "path/to/your_protobuf_module.py"
  }
}
```

## 3 客户端

### 3.1 Python

TODO

### 3.2 C++

需结合C++接口locapic使用

locapic，借助pybind11的嵌入式Python解释器，提供了一套通用的C++接口使用locapip

TODO

## 4 自定义模块

服务端和客户端的具体实现方法，请参阅```test.py```源码，以及 [gRPC Python](https://grpc.io/docs/languages/python/)
和 [Examples](https://github.com/grpc/grpc/tree/master/examples)

服务端和客户端都应能够访问同一版本的protobuf模块，因此配置文件中定义的模块名称和路径应相同