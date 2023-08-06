# {NAME}

请补充项目工程描述信息

## 项目结构

```
{NAME}
├── app                              # 源代码路径
│   ├── app_logger.py                # LOG
│   ├── app_product.py               # 多环境，配置在 Package.json
│   ├── app.py                       # 程序入口
│   └── __init__.py
├── Dockerfile.dev                   # Dev 环境 - 源码
├── Dockerfile.product               # 生产环境 - 二进制包
├── main.py                          # 项目入口
├── package.json                     # 配置信息
├── README.md                        # 说明
├── requirements.txt                 # 依赖  
└── static                           # 静态文件
    └── README.md
```

## 项目构建

**测试**
```
# 打包-源码包
roictl build-dev
# 发布-源码包，包名版本号自动添加 -dev
roictl release-dev 
# 镜像
docker build -f Dockerfile.dev -t {DOCKER_IMAGE}:latest-dev .
```

**发布**

```
# 打包-二进制包
roictl build
# 发布-二进制包
roictl release
# 镜像
docker build -f Dockerfile.product -t {DOCKER_IMAGE}:latest .
```

## 项目部署

VERSION = 1.0

```
docker build -f Dockerfile.product -t {DOCKER_IMAGE}:VERSION .
```
