# Windows10 基础开发环境


## 基础开发环境
### VS Code
### Putty等远程连接

## WSL

## Python

### pip & virtualenv 

https://note.qidong.name/2018/03/python-data-analyze-init/

### Anaconda
约需要2.6GB空间

- 设置环境变量
控制面板\系统和安全\系统\高级系统设置\环境变量\用户变量\PATH 中添加 anaconda的安装目录的Scripts文件夹 
```text
D:\Anaconda3;
D:\Anaconda3\Library\mingw-w64\bin;
D:\Anaconda3\Library\usr\bin;
D:\Anaconda3\Library\bin;
D:\Anaconda3\Scripts;
```
- PoswerShell似乎不支持, 如下命令在Command Prompt中执行
- 命令行输入`conda --version`以确认设置成功
- `conda upgrade --all -y` 先把所有工具包进行升级

### 管理虚拟环境

```
activate # 默认进入anaconda自带的base环境 
deactivate python34 # 返回默认的python环境，运行
conda create --name python34 python=3.4 -y #创建名为python34, python版本为3.4的环境, conda会自动找3.4中最新的版本下载
conda env list # 列出所有环境
conda info -e
conda remove --name test --all # 卸载环境
conda install requests # 安装第三方包
conda update requests # 更新requests包
conda remove requests # 卸载第三方包
conda list # 查看当前环境中已安装的包和对应版本
conda env export > environment.yaml # 导出当前环境的包信息可以用
conda env create -f environment.yaml // 用配置文件创建新的虚拟环境

conda env create -f environment.yaml
```


