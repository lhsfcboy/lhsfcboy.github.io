# CentOS 6 配置python环境

## 确认基本安装信息

```console
# which python
/usr/bin/python

# python --version
Python 2.6.6

cat /etc/redhat-release
## CentOS release 6.9 (Final)

yum -y groupinstall 'Development Tools'
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel

## CentOS下需要注意 Django需要sqlite的支持, 编译安装Python前
yum -y install sqlite-devel
```

## 安装思路

- 只安装python3
- 尽量使用yum安装
- 不允许修改CentOS自带的py2.6

## 编译安装python3

```console
## 下载 Python3代码包
wget  https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
tar zxf Python-3.6.5.tgz
#  rm -f Python-3.6.5.tgz
cd Python-3.6.5/
./configure
make && make install
## 注意这两行提示
Installing collected packages: setuptools, pip
Successfully installed pip-9.0.3 setuptools-39.0.1

## 验证安装
# python3.6 -V
Python 3.6.5

# ls -l /usr/local/bin/python3*
/usr/local/bin/python3 -> python3.6
/usr/local/bin/python3.6
/usr/local/bin/python3.6-config -> python3.6m-config
/usr/local/bin/python3.6m
/usr/local/bin/python3.6m-config
/usr/local/bin/python3-config -> python3.6-config

# ls -l /usr/local/bin/pip*
/usr/local/bin/pip3
/usr/local/bin/pip3.6

## 配置 pip
ln -s /usr/local/bin/pip3 /usr/local/bin/pip
pip install --upgrade pip
```

## virtualenv

```console
# pip install virtualenv
# virtualenv test_venv
# tree test_venv/ -L 2
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

## virtualenvwrapper

virtualenv 的一个最大的缺点就是，每次开启虚拟环境之前要去虚拟环境所在目录下的 bin 目录下 source 一下 activate，这就需要我们记住每个虚拟环境所在的目录。

一种可行的解决方案是，将所有的虚拟环境目录全都集中起来，比如放到 ~/virtualenvs/，并对不同的虚拟环境使用不同的目录来管理。virtualenvwrapper 正是这样做的。

```console
# pip install virtualenvwrapper

# find / -name virtualenvwrapper.sh
/usr/local/bin/virtualenvwrapper.sh


## 配置环境变量
# vim ~/.bashrc
export WORKON_HOME='~/.virtualenvs'
source /usr/local/bin/virtualenvwrapper.sh

## WORKON_HOME 就是它将要用来存放各种虚拟环境目录的目录




```

- 查看所有的命令：virtualenvwrapper --help
- 创建基本环境：mkvirtualenv [环境名]
  - mkvirtualenv --python=/usr/bin/python2.7 testenv
- 删除环境：rmvirtualenv [环境名]
- 激活环境：workon [环境名]
- 退出环境：deactivate
- 列出所有环境：workon 或者 lsvirtualenv -b

## 配置python2.7

```text
wget https://www.python.org/ftp/python/2.7.15/Python-2.7.15.tgz
tar zxf Python-2.7.15.tgz
cd Python-2.7.15
./configure
make && make install

## 默认 Python 2.7.15 会安装在 /usr/local/bin 目录下。

ll -tr /usr/local/bin/python*

/usr/local/bin/python2.7
/usr/local/bin/python2.7-config
/usr/local/bin/python -> python2
/usr/local/bin/python2 -> python2.7
/usr/local/bin/python2-config -> python2.7-config
/usr/local/bin/python-config -> python2-config

```

## 通过yum安装python3

```console
yum install -y https://centos6.iuscommunity.org/ius-release.rpm
yum install -y python36*
ln -s /usr/bin/python3.6 /usr/bin/python3
ln -s /usr/bin/pip3.6 /usr/bin/pip3
```
