# Windows10 基础开发环境

## WSL

## Python

### Anaconda
约需要2.6GB空间

- 设置环境变量
控制面板\系统和安全\系统\高级系统设置\环境变量\用户变量\PATH 中添加 anaconda的安装目录的Scripts文件夹 
"""text
D:\Anaconda3;
D:\Anaconda3\Library\mingw-w64\bin;
D:\Anaconda3\Library\usr\bin;
D:\Anaconda3\Library\bin;
D:\Anaconda3\Scripts;
""""
- 命令行输入`conda --version`以确认设置成功
- `conda upgrade --all` 先把所有工具包进行升级
