

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
