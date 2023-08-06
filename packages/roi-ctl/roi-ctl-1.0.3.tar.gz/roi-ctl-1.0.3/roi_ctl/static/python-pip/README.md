# {NAME}

模块描述，自行补充


## 工程说明

```
{NAME}
├── LICENSE                    # 版权
├── package.json               # 项目配置
├── {PACKAGE_NAME}             # 包名
│   ├── app_logger.py          # LOG 工具
│   ├── app.py                 # 程序入口
│   ├── __init__.py            
│   └── static                 # 静态资源文件夹
│       └── README.md
├── README.md                  # 项目说明
├── RELEASE.md                 # 版本说明
└── requirements.txt           # 依赖
└── static
    └── README.md
```

## 构建说明


**测试**

```
# 打包-源码包
roictl build-dev
# 发布-源码包，包名版本号自动添加 -dev
roictl release-dev 
```

**发布**

```
# 打包-二进制包
roictl build
# 发布-二进制包
roictl release
```

## 安装说明

```
roictl install {NAME}
```

## 使用说明

功能清单，自行补充