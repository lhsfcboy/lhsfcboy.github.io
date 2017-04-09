@echo off
 
set _remote_ip=192.168.137.128
set _remote_file_dir=/home/software
set _remote_username=root
set _remote_password=sy31214
set _local_file_dir=D:\
set _today=%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%
 
ping -n 1 %_remote_ip%>nul
 
pscp -l %_remote_username% -pw %_remote_password% %_remote_ip%:%_remote_file_dir%/cmake-3.3.0-rc4.tar.gz %_local_file_dir%　>out.txt
 
set /p out_status=<out.txt
 
if "%out_status:~-4%"=="100%"(
  echo "%_today%数据库备份文件下载成功"
)




