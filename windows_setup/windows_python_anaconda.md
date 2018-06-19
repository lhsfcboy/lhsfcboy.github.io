# Windows 下使用 Anaconda 配置 python 环境

下载地址: [Windows Python Environment](https://www.continuum.io/downloads)

- Spyder: 轻量级的Python开发环境
- Jupyter QTConsole: IPython

```console
pip list --format=legacy --outdated | awk '{print $1}' | xargs pip install --upgrade
pip list --format=columns --outdated | tail -n +3 | cut -d' ' -f 1 | xargs pip install --upgrade
```

```console
# 创建一个名为python34的环境，指定Python版本是3.4（不用管是3.4.x，conda会为我们自动寻找3.4.x中的最新版本）
conda create --name python34 python=3.4

# 安装好后，使用activate激活某个环境
activate python34 # for Windows
source activate python34 # for Linux & Mac
# 激活后，会发现terminal输入的地方多了python34的字样，实际上，此时系统做的事情就是把默认2.7环境从PATH中去除，再把3.4对应的命令加入PATH

# 此时，再次输入
python --version
# 可以得到`Python 3.4.5 :: Anaconda 4.1.1 (64-bit)`，即系统已经切换到了3.4的环境

# 如果想返回默认的python 2.7环境，运行
deactivate python34 # for Windows
source deactivate python34 # for Linux & Mac

# 删除一个已有的环境
conda remove --name python34 --all
```

## 命令一览

| Task                                 | Conda package and environment manager command       |
|--------------------------------------|-----------------------------------------------------|
| Install a package                    | conda install $PACKAGE_NAME                         |
| Update a package                     | conda update --name $ENVIRONMENT_NAME $PACKAGE_NAME |
| Update package manager               | conda update conda                                  |
| Uninstall a package                  | conda remove --name $ENVIRONMENT_NAME $PACKAGE_NAME |
| Create an environment                | conda create --name $ENVIRONMENT_NAME python        |
| Activate an environment              | source activate $ENVIRONMENT_NAME                   |
| Deactivate an environment            | source deactivate                                   |
| Search available packages            | conda search $SEARCH_TERM                           |
| Install package from specific source | conda install --channel $URL $PACKAGE_NAME          |
| List installed packages              | conda list --name $ENVIRONMENT_NAME                 |
| Create requirements file             | conda list --export                                 |
| List all environments                | conda info --envs                                   |
| Install other package manager        | conda install pip                                   |
| Install Python                       | conda install python=x.x                            |
| Update Python                        | conda update python *                               |

用户安装的不同python环境都会被放在目录~/anaconda/envs下，可以在命令中运行conda info -e查看已安装的环境，当前被激活的环境会显示有一个星号或者括号。

第一步：通过conda clean -p来删除没用的包，这个命令会检查哪些包没有在包缓存中被硬依赖到其他地方，并删除它们。第二步：通过conda clean -t可以将conda保存下来的tar包。

Create virtual environemnt with conda:
conda env list        #conda info -e
which python
conda create -n py27 python=2.7
source activate py35
which python
source deactivate

conda install -n py27 lxml         #需要管理员权限
conda remove -n env_name --all        #来删除指定的环境
conda install -n py27 anaconda        #为新添加的环境也装上Anaconda的科学计算包

[Anaconda install at Linux](https://www.youtube.com/watch?v=9TsPWlVTzv4)
