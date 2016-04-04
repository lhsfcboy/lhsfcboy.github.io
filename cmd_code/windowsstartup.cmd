@ECHO OFF

#尝试后台启动VB虚拟机
cd "C:\Program Files\Oracle\VirtualBox\"
VBoxHeadless startvm CentOS6.6_Dev  


#关闭OneNote烦人的提示页
taskkill /f /im onenotem.exe

EXIT
