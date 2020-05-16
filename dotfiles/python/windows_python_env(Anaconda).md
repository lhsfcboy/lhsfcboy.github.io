# 搭建Windows下的Python环境

## 安装

下载地址: [Windows Python Environment](https://www.continuum.io/downloads)

- anaconda安装路径不要出现空格
- 选择空间大的硬盘
- 把Anaconda加入环境变量
- 设置Anaconda所带的Python 3.6为系统默认的Python版本
- 打开cmd测试一下安装结果

Anaconda组件:

- Spyder: 轻量级的Python开发环境
- Jupyter QTConsole: IPython

## 使用Conda进行虚拟环境管理

Anaconda多环境多版本python配置指导 <https://www.jianshu.com/p/d2e15200ee9b>

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

## IPython

### 测试当前是否运行在ipython实例当中

```python
def in_ipynb():
    try:
        cfg = get_ipython().config
    except NameError:
        return False
    return True
in_ipynb()
```

### convert a IPython Notebook into a Python file

```python
!jupyter nbconvert --to script con.ipynb
# This command will generate con.py
```

## Jupyter Notebook

### jupyter的基础设置

><https://stackoverflow.com/questions/35254852/how-to-change-the-jupyter-start-up-folder>

### 添加环境变量

```path
D:\Program\Anaconda3;D:\Program\Anaconda3\Scripts;
```

默认的安装地址是`C:\Users\xxx\Anaconda3\Scripts`

### ipython配置文件所在地

```cmd
C:\Users\Mike\.ipython\profile_default\ipython_config.py
~/.ipython/profile_default/ipython_config.py
```

### 创建jupyter的配置文件

Open cmd (or Anaconda Prompt) and run `jupyter notebook --generate-config`.
This writes a file to `C:\Users\username\.jupyter\jupyter_notebook_config.py`.

### 修改默认启动目录

```python
#c.NotebookApp.notebook_dir = ''
c.NotebookApp.notebook_dir = '/the/path/to/home/folder/'
# c.NotebookApp.notebook_dir = "D:\GitHubWorkSpace"
```

如果从快捷方式打开Jupyter, 则将 起始位置(S) 清空, 并将 目标(T) 中的结尾的 %USERPROFILE% 删除

### 其他选项

```python
c.NotebookApp.open_browser = False # 勝手にブラウザが立ち上がらないように

# lines of code to run at IPython startup.
c.InteractiveShellApp.exec_lines = ['%matplotlib inline']

# Run all nodes interactively
c.InteractiveShell.ast_node_interactivity = "all"
# 所有的Jupyter实例（Notebook和Console）都设置该选项

## 临时启动该选项
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```

### Windows 10 修改启动目录

- Click on the Start Menu, then All Programs (just Programs for Win10)
- Click on the Anaconda3 folder; mine is Anaconda3 (64-bit)
- In there you should see Jupyter Notebook.
  - If you have a virtual environment installed, it will be followed by the environment name like this: Jupyter Notebook (env)
- Right-click Jupyter Notebook entry and navigate to More => Open File Location
- Right-click the correct Jupyter Notebook entry, then click on Properties
- Enter a path in the Start in: box; if the path has spaces in it, you must enclose it in double quotes

### jupyter-themes

><https://github.com/dunovank/jupyter-themes>
