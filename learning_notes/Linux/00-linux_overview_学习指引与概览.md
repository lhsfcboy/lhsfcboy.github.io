# 纯粹的实用导向的Linux学习

Linux在工程实践中很多时候时作为运行平台。
大部分场景下开发平台依然是Windows。
对于Linux的学习，先以实用为导向！

## 只学习自带的命令

非常有可能在一台陌生的主机上工作，且通常都不能自由安装其他命令。

## 利用好 Man Pages

- [echo(1) ](https://man7.org/linux/man-pages/man1/echo.1.html)
- [printf(3) ](https://man7.org/linux/man-pages/man3/printf.3.html)

## 入门教程

- 《Linux 101》作者：中国科学技术大学 Linux 用户协会
  - https://101.lug.ustc.edu.cn/
  - 排版精美

- Bash 脚本教程 作者： 阮一峰
  - 发布说明：https://www.ruanyifeng.com/blog/2020/04/bash-tutorial.html
  - 阅读页面：https://wangdoc.com/bash/

## 参考的学习大纲

### 1. Linux 基础介绍

- 学习总览

### 2. Linux 系统安装与基本操作

- Linux 系统的安装步骤
  - 使用VirtualBox创建虚拟机
  - 使用Vagrant/VirtualBox 创建虚拟机
- 命令行基础操作
  - 如何打开终端
  - 用户和权限概念

### 3. 文件系统基础

- Linux 文件系统结构介绍
- 绝对路径和相对路径
- 常用目录（如 `/etc/`、`/var/`、`/home/` 等）
- 文件的创建、删除与重命名
  - `touch`、`rm`、`mv`、`cp` 命令
- Linux标准输入输出与管道  

### 4. 文件与目录管理

- 文件的查看：`ls` 命令
- 文件的复制、移动与删除：`cp`、`mv`、`rm`
- 创建目录：`mkdir` 命令
- 修改文件权限与所有者：`chmod`、`chown`

### 5. 文本文件的查看与编辑

- 文件内容查看：`cat`、`less`、`more`
- 文本文件搜索：`grep`
- 文本文件剪切与格式化：`cut`、`awk`
- 简单文本编辑器：`nano`、`vim`
  - `vim` 的基本操作模式

### 6. 用户和组管理

- 用户的添加与删除：`useradd`、`userdel`
- 用户组的管理：`groupadd`、`groupdel`
- 切换用户：`su`、`sudo` 命令
- 修改用户密码：`passwd`

### 7. 文件权限与访问控制

- 文件权限的概念与表示方式（rwx）
- 文件权限的修改：`chmod`
- 文件所属用户和组的更改：`chown`、`chgrp`
- 文件和目录的权限设置及案例分析

### 8. 软件包管理

- 包管理工具的介绍（如 `apt`、`yum`）
- 软件包的安装、删除与更新
  - `apt-get install`、`yum install`
- 查找软件包：`apt search`、`yum search`
- 源列表的管理

### 9. 进程管理与调试

- 查看系统进程：`ps`、`top`、`htop`
- 后台进程管理：`&`、`bg`、`fg`、`jobs`
- 进程的优先级：`nice`、`renice`
- 终止进程：`kill`、`pkill`

### 10. 磁盘管理与挂载

- 磁盘分区与格式化：`fdisk`、`mkfs`
- 挂载和卸载文件系统：`mount`、`umount`
- 查看磁盘使用情况：`df`、`du`
- 文件系统检查与修复：`fsck`

### 11. 网络配置与管理

- 查看和配置网络：`ifconfig`、`ip`、`netstat`
- 网络连接测试：`ping`、`traceroute`
- 使用 SSH 进行远程管理：`ssh` 命令
- 文件传输工具：`scp`、`rsync`

### 12. Shell 编程基础

- 什么是 Shell 脚本？
- 编写简单的 Shell 脚本
- 变量与控制结构（条件语句、循环）
- 常用 Shell 脚本的编写与执行
  - 文件备份脚本示例
  - 系统监控脚本示例
