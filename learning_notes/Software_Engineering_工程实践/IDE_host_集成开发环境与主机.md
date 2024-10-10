# 集成开发环境与主机

## Windows系统

需要集成常用的Linux命令

### 安装 GitBash (推荐的做法)
https://www.pascallandau.com/blog/setting-up-git-bash-mingw-msys2-on-windows/

### WSL1 (Windows Subsystem for Linux)

https://www.pascallandau.com/blog/setting-up-git-bash-mingw-msys2-on-windows/

## Linux系统
如果需要完整的Linux环境，可以尝试以下几种方案：

### 方案：硬件直接安装Linux

包括 双系统 和 Linux-Only 的安装。在现在已经不推荐了

### 方案：Docker容器
- 配置复杂，理解难度高

### 方案：Vagrant管理下的VirtualBox虚拟机
- 类似方案还有VMWare的个人免费版
- 启动VM需要花时间，可以考虑设置开机启动

### 方案：免费的云主机
- 注册苦难
- 免费的额度通常有限，需要小心超额
- 依赖网络连接, 但是在现代的互联网环境下已经不算问题

### WSL2
可以粗略理解为微软定制版的Linux虚拟机，依赖Hyper-V