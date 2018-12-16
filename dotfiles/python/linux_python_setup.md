# linux环境下的python配置

不使用Anaconda

## pip等基础包

upgrade全部包

```console
pip list --format=legacy --outdated | awk '{print $1}' | xargs pip install --upgrade
pip list --format=columns --outdated | tail -n +3 | cut -d' ' -f 1 | xargs pip install --upgrade
```

## 准备虚拟环境相关工具

- virtualenv: 创建隔绝的Python环境的工具
- virtualenvwrapper: 对virtualenv的一层包装

```bash
wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
python get-pip.py
pip install virtualenv
virtualenv --version
pip install virtualenvwrapper
```

## 基本使用

```bash
cd my_project_folder
virtualenv my_project
# virtualenv my_project 将会在当前的目录中创建一个文件夹，
# 包含了Python可执行文件， 以及 pip 库的一份拷贝

virtualenv -p /usr/bin/python2.7 my_project
# 可以选择使用一个Python解释器来创建


# 激活虚拟环境
source my_project/bin/activate

# 停用
```

## virtualenvwrapper

```bash
pip install virtualenvwrapper
export WORKON_HOME=~/Envs
source /usr/local/bin/virtualenvwrapper.sh

# 创建一个虚拟环境
mkvirtualenv my_project
# WORKON_HOME中创建 my_project 文件夹
mkvirtualenv --python=python3.6 p36


# 在虚拟环境上工作
workon my_project

# 停止
deactivate

# 删除
rmvirtualenv my_project

# 列举所有的环境
lsvirtualenv

# 查看环境里安装了哪些包
lssitepackages
```

## 设置提示符样式

```console
$ cat ~/.virtualenvs/postactivate
#!/bin/bash
# This hook is sourced after every virtualenv is activated.

PS1="\[\e[1;33;45m\](`basename \"$VIRTUAL_ENV\"`)\[\e[0m\]$_OLD_VIRTUAL_PS1"
```
