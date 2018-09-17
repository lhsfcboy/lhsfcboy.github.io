# centos6.9 with mysql5.7

## 安装

```text

yum -y remove mysql*
rm -rf /etc/mysql /var/lib/mysql

rpm -qa | grep mysql

rpm -ivh https://dev.mysql.com/get/mysql57-community-release-el6-9.noarch.rpm

sudo yum install -y mysql-community-server

cp -p /etc/my.cnf /etc/my.cnf.orig
vi /etc/my.cnf

[mysqld]
character-set-server = utf8    # 编码设置
validate_password = off        # 关闭密码策略
lower_case_table_names=1       # 在SQL查询中忽略表的大小写


service mysqld start

grep 'temporary password' /var/log/mysqld.log

mysql_secure_installation
## 这里设置的新密码必须满足 大写字母+小写字母+数字+特殊字符
```

## 基础设置

```text
mysql --version

service mysqld status
service mysqld restart

mysql -u root --skip-password
ALTER USER 'root'@'localhost' IDENTIFIED BY 'root123';

chkconfig mysqld on
chkconfig | grep mysqld
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
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'root123' WITH GRANT OPTION;

--允许用户jack从ip为10.10.50.127的主机连接到mysql服务器，并使用654321作为密码
GRANT ALL PRIVILEGES ON *.* TO 'jack'@’10.10.50.127’ IDENTIFIED BY '654321' WITH GRANT OPTION;

-- 赋予任何主机访问数据的权限
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```
