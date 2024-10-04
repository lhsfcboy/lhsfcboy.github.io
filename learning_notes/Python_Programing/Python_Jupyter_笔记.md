## 配置jupyter环境

### 安装

使用python2.7进行安装
> pip install jupyter

或者
> pip install --upgrade  --force-reinstall  --no-cache-dir  jupyter

### 启动

> jupyter notebook --allow-root

## 测试当前是否运行在ipython实例当中
```Python
def in_ipynb():
    try:
        cfg = get_ipython().config 
    except NameError:
        return False
    return True
in_ipynb()
```

## convert a IPython Notebook into a Python file 
```shell
!jupyter nbconvert --to script con.ipynb
# This command will generate con.py
```

## jupyter-themes
https://github.com/dunovank/jupyter-themes

## jupyter的基础设置

https://stackoverflow.com/questions/35254852/how-to-change-the-jupyter-start-up-folder

### 添加环境变量

```path
D:\Program\Anaconda3;D:\Program\Anaconda3\Scripts;
```

默认的安装地址是`C:\Users\xxx\Anaconda3\Scripts`

### ipython配置文件所在地

```shell
C:\Users\Mike\.ipython\profile_default\ipython_config.py
~/.ipython/profile_default/ipython_config.py
```

### 创建jupyter的配置文件

```
Open cmd (or Anaconda Prompt) and run jupyter notebook --generate-config.
This writes a file to C:\Users\username\.jupyter\jupyter_notebook_config.py.
```

### 修改默认启动目录

```python
#c.NotebookApp.notebook_dir = ''
c.NotebookApp.notebook_dir = '/the/path/to/home/folder/'
# c.NotebookApp.notebook_dir = "D:\GitHubWorkSpace"
```

如果从快捷方式打开Jupyter, 则将 起始位置(S) 清空, 并将 目标(T) 中的结尾的 %USERPROFILE% 删除

### 其他选项

```shell
c.NotebookApp.open_browser = False # 阻止Jupyter使用浏览器

# lines of code to run at IPython startup.
c.InteractiveShellApp.exec_lines = ['%matplotlib inline']

# Run all nodes interactively
c.InteractiveShell.ast_node_interactivity = "all"
# 所有的Jupyter实例（Notebook和Console）都设置该选项

临时启动该选项
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
