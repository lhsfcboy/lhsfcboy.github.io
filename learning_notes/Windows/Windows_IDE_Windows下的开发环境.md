# Windows下的开发环境

## Git Bash 的安装

## Git Bash 的基础配置

### 提示符PS1的显示

- 当前目录有变化时,在PS1中显示一个星号
```bash
export GIT_PS1_SHOWDIRTYSTATE=1
```
### 显示中文乱码
- 在git bash下，右键 选择options，选择“Text”，将“Character set”设置为  UTF-8


## 配置的生效

即刻生效各类配置 
```bash
source ~/.bashrc
```

## 增添常用的Linux命令

```
Add wget command
https://eternallybored.org/misc/wget/
C:\Program Files\Git\mingw64\bin\

Add Tree Command
Download from http://gnuwin32.sourceforge.net/packages/tree.htm
and unzip exe to C:\Program Files\Git\usr\bin

Download Files
默认没有安装wget 可以使用curl -O 来下载文件
curl -k https://www.example.com/file.txt -o file.txt
```
