# CentOS 6.5 上安装配置 MySQL 5.1

CentOS的yum中的MySQL是5.1, 我们通过yum来安装配置.

## MYSQL

```text
rpm -qa | grep mysql
yum remove mysql*
yum list | grep mysql
yum install -y mysql-server
yum install -y mysql-server mysql mysql-devel

rpm -qa | grep mysql
rpm -qi mysql-server

service mysqld start
chkconfig --list | grep mysqld
chkconfig mysqld on
chkconfig --list | grep mysqld


/usr/bin/mysqladmin -u root password 'new-password'
##注意新密码是单引号包括起来的部分
mysql -u root -p

# 设置root远程连接
# 1, 从所有主机
mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'rootpassword' WITH GRANT OPTION;
# 2, 从指定主机：
mysql> grant all privileges on *.* to root@"192.168.11.205" identified by"root用户的密码"with grant option; flush privileges;

netstat -anp | grep 3306

/sbin/iptables -I INPUT -p tcp --dport 3306 -j ACCEPT
/etc/rc.d/init.d/iptables save
/etc/init.d/iptables restart

vi /etc/my.cnf #添加如下内容以支持中文
[client]
default-character-set = utf8
[mysql]
default-character-set = utf8
[mysqld]
character-set-server = utf8
init-connect='set names utf8'


service mysqld restart

# 从远端测试连接
nc -z -w1 192.168.56.10 3306
echo X | telnet -e X 192.168.56.10 3306
mysql -u usernmae -h 65.55.55.2 -p
```

## PHPmyadmin

```text
yum -y install httpd
chkconfig httpd on
chkconfig --list httpd
iptables -I INPUT -p tcp --dport 80 -j ACCEPT
service iptables save
http://123.45.67.89

yum -y install php
## php 不包含在CentOS Minimal之中
## 而且yum中竟然不是phpmyadmin的依赖项

# 安装EPEL https://dl.fedoraproject.org/pub/epel/6/x86_64/
curl -O https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
sudo rpm -ivh epel-release*
yum repolist
vi /etc/yum.repos.d/epel.repo
    enabled=0
yum --enablerepo=epel -y install phpMyAdmin php-mysql php-mcrypt


vi /etc/httpd/conf.d/phpMyAdmin.conf
# 分别为 /usr/share/phpMyAdmin/ 和 /usr/share/phpMyAdmin/setup/
# 如下设置, 以启用远程连接

# Deny from all ## 注释掉"Deny from all"
Allow from 0.0.0.0 ## 修改Allow from 127.0.0.1

/etc/rc.d/init.d/httpd restart

http://<web-server-ip-addresss>/phpmyadmin


# 设置session的失效时间
## 默认的是1440
vi /etc/php.ini
session.gc_maxlifetime = 1440
## 修改为
session.gc_maxlifetime = 144000

vi /usr/share/phpMyAdmin/libraries/config.default.php
$cfg['LoginCookieValidity'] = 1440;
## 修改为
$cfg['LoginCookieValidity'] = 144000;

## 注意: phpMyAdmin的有效期不能长于php本身的有效期

```