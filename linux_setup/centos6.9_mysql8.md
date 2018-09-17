# centos6.9 with mysql8

!!!WIP!!!

尚未验证成功安装, mysql8推荐在CentOS7上安装

## 准备libstdc++

mysql8需要的GLIBCXX版本高于CentOS6.9自带

```text
## https://www.saintsouth.net/blog/update-libstdcpp-on-centos6/
## http://dotnsf.blog.jp/archives/1064353059.html

strings /usr/lib64/libstdc++.so.6 | grep GLIBCXX
## 查看libstdc++

yum install -y gmp-devel mpfr-devel libmpc-devel
yum install -y glibc-devel.i686
## Even on a x64 machine, i686 is required


## gcc
mkdir -p ~/src
cd ~/src
curl -LO http://ftp.tsukuba.wide.ad.jp/software/gcc/releases/gcc-4.8.4/gcc-4.8.4.tar.gz
tar fxz gcc-4.8.4.tar.gz
cd gcc-4.8.4

## !!!特别花时间!!!
./configure
make

ls -l /usr/lib64/libstd*
cp ${HOME}/src/gcc-4.8.4/x86_64-unknown-linux-gnu/libstdc++-v3/src/.libs/libstdc++.so.6.0.19 /usr/lib64

cd /usr/lib64
sudo mv libstdc++.so.6 libstdc++.so.6.bak
sudo ln -s libstdc++.so.6.0.19 libstdc++.so.6
ls -l /usr/lib64/libstd*


strings /usr/lib64/libstdc++.so.6 | grep GLIBCXX
```

## 安装

```text
sudo service mysqld stop

yum -y remove mysql*
rpm -qa | grep mysql
sudo yum remove mysql-community-release.noarch

## https://dev.mysql.com/downloads/repo/yum/
sudo rpm -Uvh https://dev.mysql.com/get/mysql80-community-release-el6-1.noarch.rpm
yum repolist all | grep mysql

yum install mysql-community-server


mysql --version
```

## 基础设置

```text
mysql --version
service mysqld status
service mysql start
chkconfig mysqld on
chkconfig | grep mysqld
```

## 数据库设置

```text
mysql -u root

```

## 允许mysql远程访问

有如下方式, 首先确认现有的权限

```sql
USE mysql
select host, user from user;
```

### 1,改表

```sql
update user set host = '%' where user = 'root';
```

### 2,赋权

```sql
--root使用123456从任何主机连接到mysql服务器。
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;

--允许用户jack从ip为10.10.50.127的主机连接到mysql服务器，并使用654321作为密码
GRANT ALL PRIVILEGES ON *.* TO 'jack'@’10.10.50.127’ IDENTIFIED BY '654321' WITH GRANT OPTION;

-- 赋予任何主机访问数据的权限
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```
