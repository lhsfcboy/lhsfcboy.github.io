# what we should do after a new server is avaliable

## 确认基本安装信息

```text
uname -i
rpm -q kernel
cat /etc/redhat-release


# 关闭SeLinux
setenforce 0
/etc/selinux/config
    SELINUX=disabled

yum -y update && yum -y upgrade
```

## From Minimal Install

```text
yum -y groupinstall 'Development Tools'
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel
# yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
yum -y install wget
yum -y install telnet

yum -y install man

```

## Web相关

```text
yum -y install httpd

yum -y install links ## 命令行 Web 浏览器
links 127.0.0.1 ## 检查本机的httpd

yum -y install php
echo -e "<?php\nphpinfo();\n?>"  > /var/www/html/phpinfo.php
links http://127.0.0.1/phpinfo.php
```

## From EPEL

```text

rpm -ivh http://ftp-srv2.kddilabs.jp/Linux/distributions/fedora/epel/6/x86_64/epel-release-6-8.noarch.rpm
## epel-release-6-8.noarch.rpm

yum --enablerepo=epel -y install htop

```

## SSH相关

```console
/etc/ssh/sshd_config ClientAliveInterval
service sshd reload
```

## Selfmonitoring Tool

### 进程管理

yum -y install htop

### 磁盘管理 disk usage

yum -y install ncdu

### 网络端口监视

yum -y install nmap

### 网络流量监视
yum -y install iftop