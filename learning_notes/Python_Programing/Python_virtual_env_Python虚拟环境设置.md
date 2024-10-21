# Python虚拟环境的设置

## 所谓全局环境

- pip: python的包管理工具，可以用于安装python包。

## Windows下安装Python

**不要**通过 Microsoft Store 安装Python，它使用了一个沙盒环境来隔离应用程序，路径会比较特殊。
`C:\Users\lhsfc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts`是 Microsoft Store 版本的 Python 的标准安装位置。
  
## 主流的环境管理工具

- conda: python虚拟环境管理工具，其中一个功能是安装python包。
- miniconda: conda的压缩包，自带了一个名为base的虚拟环境，这个虚拟环境里只安装了python和几个必要的库。
- anaconda：conda的压缩包。自带了一个名为base的虚拟环境，这个虚拟环境里安装了很多和数据处理有关的python包。


- https://www.zhihu.com/question/404402864
- https://sspai.com/post/75978
- https://note.com/e2718/n/n4d1bf2110990
- https://github.com/walter201230/Python/blob/master/Article/advanced/%E4%BD%BF%E7%94%A8Python%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83.md
- https://pyloong.github.io/pythonic-project-guidelines/introduction/virtualenv/
- https://pythonguidecn.readthedocs.io/zh/latest/dev/virtualenvs.html
- https://www.bilibili.com/read/cv33621531/
- https://liaoxuefeng.com/books/python/built-in-modules/venv/
- https://www.freecodecamp.org/chinese/news/how-to-setup-virtual-environments-in-python/
- https://sspai.com/post/82499
- https://zhuanlan.zhihu.com/p/663735038
- https://zhuanlan.zhihu.com/p/716634192
- https://zhuanlan.zhihu.com/p/679243801
- https://zhuanlan.zhihu.com/p/683699218
- https://www.zhihu.com/question/404402864

## 基于venv的环境管理

venv --- 创建虚拟环境

https://docs.python.org/zh-cn/3.12/library/venv.html

### Windows下的一种安装方式

- 无特殊需求的话，不再安装任何Python2版本。
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
  
## 基于Anaconda

[Anaconda多环境多版本python配置指导](https://www.jianshu.com/p/d2e15200ee9b0)
- anaconda安装路径不要出现空格
- 选择空间大的硬盘
- 把Anaconda加入环境变量
- 设置Anaconda所带的Python 3.6为系统默认的Python版本
- 打开cmd测试一下安装结果

```bash
# 检查默认的python版本
python --version
# which python

# 验证conda已被安装
conda --version
# 更新conda至最新版本
conda update conda

# 创建一个名为python34的环境，指定Python版本是3.4
# 不用管是3.4.x，conda会为我们自动寻找3.4.x中的最新版本
conda create --name p34 python=3.4
conda install -n py27 lxml # 需要管理员权限

# 在新创建的环境中创建多个包
conda create -n python3 python=3.5 numpy pandas
# 为新添加的环境也装上Anaconda的科学计算包
conda install -n py27 anaconda

# 安装好后，使用activate激活某个环境
activate python34 # for Windows
# source activate python34 # for Linux & Mac

# 激活后，会发现terminal输入的地方多了python34的字样
# 此时系统做的事情就是把默认2.7环境从PATH中去除，再把3.4对应的命令加入PATH

# 此时，再次输入
python --version
# 可以得到`Python 3.4.5 :: Anaconda 4.1.1 (64-bit)`，即系统已经切换到了3.4的环境

# 包管理
conda search --full-name python # 精确查找
conda search <text> # 查找含有此字段的包名
# 查看已经安装的包
conda list # 会显示已经安装的包名和版本号
# 在指定环境中安装包
conda install --name <env_name> <package_name>
# 在当前环境中安装包
conda install <package_name>
# 更新所有包
conda upgrade --all

# 如果想返回默认的python 2.7环境，运行
deactivate python34 # for Windows
# source deactivate python34 # for Linux & Mac

# 查看系统中的环境
conda env list
# conda info -e
# 当前被激活的环境会显示有一个星号或者括号
# 用户安装的不同python环境都会被放在目录~/anaconda/envs下


# 复制环境
conda create --name <new_env_name> --clone <copied_env_name>

# 删除一个已有的环境
conda remove --name python34 --all

# 删除没用的包
conda clean -p
# 这个命令会检查哪些包没有在包缓存中被硬依赖到其他地方, 并删除它们
```
