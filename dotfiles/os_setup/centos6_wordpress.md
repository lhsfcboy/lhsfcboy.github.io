# 安装配置WordPress

## 安装基础软件

```bash
sudo yum install httpd
sudo service httpd start

sudo yum install mysql-server
sudo service mysqld start

sudo yum install php php-mysql
yum install php-gd php-imap php-ldap php-odbc php-pear php-xml php-xmlrpc

sudo chkconfig httpd on
sudo chkconfig mysqld on
service --status-all

wget http://cn.wordpress.org/wordpress-3.9-zh_CN.zip
wget https://wordpress.org/latest.zip
unzip wordpress-3.8-zh_CN.zip
cp -rf wordpress/* /var/www/html/

sudo vim /var/www/html/info.php
```

测试用的`info.php`文件

```php
<?php
phpinfo();
?>
```

创建sql文件

```sql
#mysql -u root -p
create database wordpress;
```

```bash
find / -name wp-config-sample.php
/var/www/html/wp-config-sample.php
```


```php
/** MySQL数据库名：wordpress */
define(‘DB_NAME', ‘wordpress');
/** MySQL数据库用户名 :root*/
define(‘DB_USER', ‘root');
/** MySQL数据库密码 :password*/
define(‘DB_PASSWORD', ‘123456');
/** MySQL主机（不用修改） */
define(‘DB_HOST', ‘localhost');
```
