# 开机自动运行

## 在`init.d`文件夹中添加脚本, 之后通过`chkconfig`统一管理

脚本应当包含如下注释

```text
#add for chkconfig
#chkconfig: 2345 70 30
#description: the description of the shell   #关于脚本的简短描述
#processname: servicename                    #第一个进程名，后边设置自启动的时候会用到
```

```bash
cd /etc/init.d
vi youshell.sh
chmod +x youshell.sh
chkconfig --add servicename
```

说明：

- 2345是指脚本的运行级别，即在2345这4种模式下都可以运行，234都是文本界面，5就是图形界面X
- 70是指脚本将来的启动顺序号，如果别的程序的启动顺序号比70小（比如44、45），则脚本需要等这些程序都启动以后才启动。
- 0是指系统关闭时，脚本的停止顺序号。

```bash
# 显示系统服务列表
chkconfig –list

# 显示个别服务启动状况
chkconfig –list httpd

# 在运行级别3、4、5中停运 nscd 服务
chkconfig –level 345 nscd off
```

## 直接修改 `/etc/rc.d/rc.local`