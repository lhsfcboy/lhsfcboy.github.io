# MySQL 5.7 在Windows7下的配置

## From Installer 安装与启动

[MySQL archives installer](https://downloads.mysql.com/archives/installer/)

`mysql-installer-community-5.7.23.0.msi`

```text
- Server Only
- Path
  - Install Dir
    - D:\Program\MySQL\MySQL Server 5.7
  - Data Dir
    - D:\ProgramData\MySQL\MySQL Server 5.7
- Root Passwords
- MySQL Service Name: MySQL57
- Start the MySQL Server at System Startup
  - Disable

mysql --version
```

安装完成后, Installer会自动启动mysql服务, 并完成初始化

## From ZIP

<https://dev.mysql.com/downloads/mysql/>

- 进入解压后的目录，找到my.ini文件，修改basedir与datadir两个参数，本例如下：

```ini
    basedir = D:\MySQL\mysql-5.7.15
    datadir = D:\MySQL\mysql-5.7.15\data
```

- 进入D:\MySQL\mysql-5.7.15\bin下，依次运行

```cmd
    mysqld.exe --install MySQL
    mysqld.exe  --initialize
    net start mysql
```

使用`--initialize`时, 从`log-error`中找到随机分配的初始密码, 用于首次登陆.

```log
2018-10-04T01:19:33.166710Z 1 [Note] A temporary password is generated for root@localhost: UB_k6g9lquA1
```

## 配置

确认配置文件的位置,运行命令 `mysql --help`

```text
Default options are read from the following files in the given order:
C:\Windows\my.ini
C:\Windows\my.cnf
C:\my.ini
C:\my.cnf
C:\Program Files\MySQL\MySQL Server 5.7\my.ini
C:\Program Files\MySQL\MySQL Server 5.7\my.cnf
```

```ini
[mysql]
default-character-set = utf8mb4 ## 远程连接的mysql客户端的配置

[mysqld]
datadir=D:/ProgramData/MySQL/Data ## 确认data位置
character-set-server=utf8mb4

character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci

general_log_file="MIKE-THINK.log"
log-error="MIKE-THINK.err" ## Error Logging.
```

## 连入已经启动的MySQL

CMD 下, 导航至MySQL的bin目录. (cmd中, 变更所在硬盘, 直接输入盘符: `D:`即可)

```bash
mysql -u root -p


## 配置root远程登录

use mysql;
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'root' WITH GRANT OPTION;

## 可以在系统服务中启动关闭Mysql
## 计算机管理 | 服务和应用程序 | 服务

## 管理员权限的cmd窗口下
net stop mysql57
```


## uninstall_mysql


　　1、控制面板里的增加删除程序内进行删除

　　2、删除MySQL文件夹下的my.ini文件，如果备份好，可以直接将文件夹全部删除

　　3、开始->运行-> regedit 看看注册表里这几个地方删除没有

　　HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Eventlog\Application\MySQL 目录删除

　　HKEY_LOCAL_MACHINE\SYSTEM\ControlSet002\Services\Eventlog\Application\MySQL 目录删除

　　HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Eventlog\Application\MySQL 目录删除（我卸载的时候没有找到，略过后仍达到完全卸载的目的。）

　　4、这一条是很关键的

　　C:\Documents and Settings\All Users\Application Data\MySQL

　　这里还有MySQL的文件，必须要删除

　　注意：Application Data这个文件夹是隐藏的，需要打开个文件夹选择菜单栏 工具→文件夹选项→查看→隐藏文件和文件夹 一项选上 显示所有文件和文件夹 确定
