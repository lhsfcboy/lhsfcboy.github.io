# centos6.9 with mysql5.6

## 安装

```text
yum remove mysql*
rpm -qa | grep mysql

wget http://dev.mysql.com/get/mysql-community-release-el6-5.noarch.rpm
wget http://dev.mysql.com/get/mysql-community-release-el6-5.noarch.rpm --no-check-certificate
sudo rpm -Uvh mysql-community-release-el6-5.noarch.rpm
sudo yum install mysql-community-server
```

[yumリポジトリ](http://dev.mysql.com/downloads/repo/yum/)

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
