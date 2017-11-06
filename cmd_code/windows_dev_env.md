本文记录了Windows下的开发环境配置.


# 通用
- Notepad++
- Visual Studio Code
- ATOM
    + Sync Settings
    + Script (Ctrl+Shift+B to run script)
    + file-icons
    + minimap/
    + Themes
        predawn-ui/predawn-syntax
    + Settings
        - Editor
            + Font Family: Source Code Pro
            + Scroll Past End
            + Tab Length: 4
    + Packages
        autocomplete-python
        (Kite or local engine?)
        (instead of autocomplete-plus/autocomplete-snippets, dasable them)
        python-autopep8
            pip install autopep8
            Format on save
    + Dangerous Zone
        linter-flake8
            pip install falke8
- Git Bash
- Java 8 SDK
- Node.js
- Oracle VM VirtualBox
- Strawberry Perl

# SSH相关
## putty
## winscp

# Python
- python matplotlib 中文显示参数设置

Ref: https://segmentfault.com/a/1190000005144275
```
每次编写代码时进行参数设置
#coding:utf-8
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#有中文出现的情况，需要u'内容'

#coding:utf-8
import matplotlib.pyplot as plt
plt.plot((1,2,3),(4,3,-1))
plt.xlabel(u'横坐标')
plt.ylabel(u'纵坐标')
plt.show()
```


## Anaconda
- Spyder: 轻量级的Python开发环境
- Jupyter QTConsole: IPython
- 配置Jupyter Notebooks
    jupyter notebook config file:
```
        jupyter notebook --generate-config.
        This writes a file to C:\Users\username\.jupyter\jupyter_notebook_config.
        Change line 179 #c.NotebookApp.notebook_dir = ''
        to c.NotebookApp.notebook_dir = 'C:/Your/Desired/Start/Directory/'
        u'C:\\path\\to\\folder'

        另外Jupyter Notebook的快捷方式里面 注意删除掉 末尾的%USERPROFILE%
```

    - Conda下安装r-irkernel
    https://anaconda.org/r/r-irkernel
    在本地的Jupyter Notebooks上安装R语言的kernel
        conda install -c r r-irkernel
Anaconda多环境多版本python配置指导
    http://www.jianshu.com/p/d2e15200ee9b
    - 一般情况下的安装
    From R window：
    install.packages(c('repr', 'IRdisplay', 'crayon', 'pbdZMQ', 'devtools'))
    From teminal R command:
    devtools::install_github('IRkernel/IRkernel')
    IRkernel::installspec()

## PyCharm Community Edition

## 配置Git Bash
- 使gitbash可以使用python命令
~/.bashrc
alias python='winpty python.exe'

- 即刻生效各类配置
source ~/.bashrc

# R
## R-Studio




# Latex
Tex Live 2017
