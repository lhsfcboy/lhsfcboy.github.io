# Python虚拟环境的设置

## 所谓全局环境

- pip: python的包管理工具，可以用于安装python包。

```shell
# 显示当前安装的 pip 版本信息
pip --version
# 将当前环境中所有的非可编辑模式安装的包升级到最新版本
pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U
# 将所有已安装的、存在更新版本的 Python 包升级到最新版本
pip list --outdated | awk 'NR>2 {print $1}' | xargs pip install -U
```

## Windows下安装Python

**不要**通过 Microsoft Store 安装Python，它使用了一个沙盒环境来隔离应用程序，路径会比较特殊。
`C:\Users\lhsfc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts`是 Microsoft Store 版本的 Python 的标准安装位置。

## Python版本的考量 Python2 vs Python3

- 无特殊需求的话，不再安装任何Python2版本
- 无特殊需求的话, 使用最新版Python3版本

## 虚拟环境的管理

 虚拟环境：一个独立的Python环境，里面装了各种包，但不会安装到系统目录中。

## 主流的环境管理工具

主要参考文章

- [10.2 细数Python 虚拟环境的管理方案](https://sspai.com/post/75978)
- [『折腾指北』Python 开发环境管理](https://sspai.com/post/82499)
- [Pipenv & 虚拟环境](https://pythonguidecn.readthedocs.io/zh/latest/dev/virtualenvs.html)

其他参考文章

- https://www.zhihu.com/question/404402864
- https://note.com/e2718/n/n4d1bf2110990
- https://github.com/walter201230/Python/blob/master/Article/advanced/%E4%BD%BF%E7%94%A8Python%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83.md
- https://pyloong.github.io/pythonic-project-guidelines/introduction/virtualenv/
- https://pythonguidecn.readthedocs.io/zh/latest/dev/virtualenvs.html
- https://www.bilibili.com/read/cv33621531/
- https://liaoxuefeng.com/books/python/built-in-modules/venv/
- https://www.freecodecamp.org/chinese/news/how-to-setup-virtual-environments-in-python/
- https://zhuanlan.zhihu.com/p/663735038
- https://zhuanlan.zhihu.com/p/716634192
- https://zhuanlan.zhihu.com/p/679243801
- https://zhuanlan.zhihu.com/p/683699218
- https://www.zhihu.com/question/404402864

## 基于venv的环境管理

venv --- 创建虚拟环境

<https://docs.python.org/zh-cn/3.12/library/venv.html>

### Windows下的一种安装方式

- 安装所需要的版本到独立目录，例如
  - Python3.12 -> "C:\Python312\python.exe"
  - Python3.11 -> "C:\Python311\python.exe"
  - Python3.10 -> "C:\Python310\python.exe"
- 构建单独的venv环境

  ```cmd
  "C:\Python312\python.exe" -m venv D:\venv312-base
  "C:\Python312\python.exe" -m venv D:\venv312-project-A
  "C:\Python312\python.exe" -m venv D:\venv312-project-B
  ```

- 激活并检查

  ```cmd
  D:\venv312-base\Scripts\activate.bat
  python --version
  pip install numpy
  ```

## 基于virtualenv/virtualenvwrapper

- virtualenv: 创建隔绝的Python环境的工具
- virtualenvwrapper: 对virtualenv的一层包装

主要命令

- 查看所有的命令：virtualenvwrapper --help
- 创建基本环境：mkvirtualenv [环境名]
  - mkvirtualenv --python=/usr/bin/python2.7 testenv
- 删除环境：rmvirtualenv [环境名]
- 激活环境：workon [环境名]
- 退出环境：deactivate
- 列出所有环境：workon 或者 lsvirtualenv -b

```bash
pip install virtualenv
virtualenv test_venv
tree test_venv/ -L 2
test_venv/
├── bin
│   ├── activate
│   ├── activate.csh
│   ├── activate.fish
│   ├── activate_this.py
│   ├── easy_install
│   ├── easy_install-3.6
│   ├── pip
│   ├── pip3
│   ├── pip3.6
│   ├── python -> python3.6
│   ├── python3 -> python3.6
│   ├── python3.6
│   ├── python-config
│   └── wheel
├── include
│   └── python3.6m -> /usr/local/include/python3.6m
├── lib
│   └── python3.6
└── pip-selfcheck.json

## bin 目录中包含一些在这个虚拟环境中可用的命令，以及开启虚拟环境的脚本 activate
## include 中包含虚拟环境中的头文件，包括 Python 的头文件
## lib 中就是一些依赖库

# 激活虚拟环境
source /path/to/project/spider/bin/activate
# 退出虚拟环境
deactivate

# 删除虚拟环境
## 删掉掉目录下的 bin、include 和 lib 三个目录
```

如果没有启动虚拟环境，系统也安装了pip工具，那么套件将被安装在系统环境中，为了避免发生此事，可以在 `~/.bashrc` 文件中加上：`export PIP_REQUIRE_VIRTUALENV=true`

### virtualenvwrapper

virtualenv 的一个最大的缺点就是，每次开启虚拟环境之前要去虚拟环境所在目录下的 bin 目录下 source 一下 activate，这就需要我们记住每个虚拟环境所在的目录。

一种可行的解决方案是，将所有的虚拟环境目录全都集中起来，比如放到 ~/virtualenvs/，并对不同的虚拟环境使用不同的目录来管理。virtualenvwrapper 正是这样做的。

```bash
pip install virtualenvwrapper
find / -name virtualenvwrapper.sh

/usr/local/bin/virtualenvwrapper.sh

## 配置环境变量
# vim ~/.bashrc
export WORKON_HOME='~/.virtualenvs'
source /usr/local/bin/virtualenvwrapper.sh
## WORKON_HOME 就是它将要用来存放各种虚拟环境目录的目录

```
