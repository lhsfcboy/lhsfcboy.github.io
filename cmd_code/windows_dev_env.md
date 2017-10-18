本文记录了Windows下的开发环境配置.

# 通用
Notepad++
Visual Studio Code
ATOM
    Sync Settings
        Script (Ctrl+Shift+B to run script)
        file-icons
        minimap/
    Themes
        predawn-ui/predawn-syntax
    Settings
        Editor
            Font Family: Source Code Pro
            Scroll Past End
            Tab Length: 4
    Packages
        autocomplete-python
        (Kite or local engine?)
        (instead of autocomplete-plus/autocomplete-snippets, dasable them)
        python-autopep8
            pip install autopep8
            Format on save
    Dangerous Zone
        linter-flake8
            pip install falke8
Git Bash
Java 8 SDK
Node.js
Oracle VM VirtualBox
Strawberry Perl

# SSH相关
## putty
## winscp

# Python
## Anaconda
Spyder: 轻量级的Python开发环境
Jupyter QTConsole: IPython
配置Jupyter Notebooks
    jupyter notebook config file:
        jupyter notebook --generate-config.
        This writes a file to C:\Users\username\.jupyter\jupyter_notebook_config.
        Change line 179 #c.NotebookApp.notebook_dir = ''
        to c.NotebookApp.notebook_dir = 'C:/Your/Desired/Start/Directory/'
    在本地的Jupyter Notebooks上安装R语言的kernel
        conda install -c r r-irkernel
Anaconda多环境多版本python配置指导
    http://www.jianshu.com/p/d2e15200ee9b


## PyCharm Community Edition

## 配置Git Bash
~/.bashrc
alias python='winpty python.exe'


 source ~/.bashrc

# R
## R-Studio




# Latex
Tex Live 2017
