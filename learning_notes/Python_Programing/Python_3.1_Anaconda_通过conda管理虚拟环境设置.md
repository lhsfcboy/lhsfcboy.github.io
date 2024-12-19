# 基于Anaconda

- conda: python虚拟环境管理工具，其中一个功能是安装python包。
- miniconda: conda的压缩包，自带了一个名为base的虚拟环境，这个虚拟环境里只安装了python和几个必要的库。
- anaconda：conda的压缩包。自带了一个名为base的虚拟环境，这个虚拟环境里安装了很多和数据处理有关的python包。

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
