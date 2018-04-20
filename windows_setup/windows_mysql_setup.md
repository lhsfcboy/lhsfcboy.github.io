# MySQL 5.7 在Windows下的配置

[MySQL archives installer](https://downloads.mysql.com/archives/installer/)

## 安装与启动

安装完成后通过Windows服务来启动/关闭

## 确认配置文件的位置

运行命令 `mysql --help`

```text
Default options are read from the following files in the given order:
C:\Windows\my.ini
C:\Windows\my.cnf
C:\my.ini
C:\my.cnf
C:\Program Files\MySQL\MySQL Server 5.7\my.ini
C:\Program Files\MySQL\MySQL Server 5.7\my.cnf
```

## setup

datadir=D:/ProgramData/MySQL/Data

## utf8mb4的配置

- 确认现有编码配置
> SHOW VARIABLES WHERE Variable_name LIKE 'character\_set\_%' OR   Variable_name LIKE 'collation%';

- 使用管理员权限修改现有配置

```text
# 对其他远程连接的mysql客户端的配置
[mysql]
default-character-set = utf8mb4

# 本地mysql服务的配置
[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci
```