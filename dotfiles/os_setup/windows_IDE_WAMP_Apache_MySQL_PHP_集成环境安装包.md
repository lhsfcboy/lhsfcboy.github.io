# apache+PHP+MySQL 集成环境安装

apache+PHP+MySQL是常见php环境，在windows下也称为WAMP,对于初学者自选版本搭建总是会遇到一些麻烦，下面是收集到的一些集成环境安装：

## AppServ

<http://www.appservnetwork.com/>

软件包列表:

```text
AppServ 8.6.0
Apache 2.4.25
PHP 5.6.30
PHP 7.1.1
MySQL 5.7.17
phpMyAdmin 4.6.6
```

添加到系统中的自动启动的服务

- apache24
- mysql57

## XAMPP (功能全面)

使用说明: <https://www.cnblogs.com/qyfeng009/p/5055192.html>

<http://www.apachefriends.org/zh_cn/index.html>

XAMPP(X-系统，A-Apache，M-Mysql，P-php，P-Phpmyadmin/Perl)开源、免费的网络服务器软件，经过简单安装后，就可以在个人电脑上搭建服务器环境。

```text
MySQL 管理员（root）未设置密码。
MySQL 服务器可以通过网络访问。
PhpMyAdmin 可以通过网络访问。
样例可以通过网络访问。
Mercury 邮件服务器和 FileZilla FTP 服务器的用户是公开的。
        User: newuser   Password: wampp
        User: anonymous   Password: some@mail.net
```

### Installer

XAMPP官网的安装指导网页以供参考，网址：<http://www.apachefriends.org/zh_cn/xampp-windows.html> 或者<http://www.cnblogs.com/bnuvincent/archive/2010/11/09/1872358.html>

### ZIP / 7zip

`setup-xampp.bat`

### xampp的控制台

`xampp-control.exe`

## 其他

- WampServer
- phpstudy
- APMServ
