# Poetry

Python 虚拟环境和依赖管理工具 Poetry

<https://zhuanlan.zhihu.com/p/81025311>

## 使用 poetry创建一个新的 Python 项目

使用 poetry new <文件夹名称> 命令可以创建一个项目模板：

```shell
$ poetry new foo
这会创建一个这样的项目结构：
foo
├── pyproject.toml
├── README.rst
├── foo
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_foo.py
```
