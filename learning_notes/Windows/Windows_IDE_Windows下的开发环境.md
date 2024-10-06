# Windows下的开发环境

## 修改输入输出的文件编码为UTF-8.
> chcp 65001

## Windows 窗口与CMD的切换
- 命令行窗口时，用文件浏览器打开当前目录 `start .`
- 在文件浏览器中用终端打开当前路径 `右键` 在终端中打开
  - Win10 需要用 `Shift + 右键`
    
## Windows CMD 的基础配置

- 快速编辑模式：在Bash窗口上点右键 选择Properties，选中QuiteEditMode
  - 启用快速编辑模式后，可以直接在 Git Bash 窗口中通过鼠标右键来复制和粘贴文本
  - 选择文本：你可以通过左键单击并拖动鼠标来选择文本，松开鼠标后，选择的文本会自动复制到剪贴板
  - 粘贴文本：右键单击 Bash 窗口，将剪贴板中的内容粘贴到当前光标位置。
- 同样的位置设置插入模式InsertMode复选框勾上
  - 插入模式下，输入的文本将插入到当前光标所在位置，而不会替换光标后的文本
- 按行显示PATH
```cmd
echo %PATH:;=&echo.%
```

## Windows CMD 下的磁盘操作

- 创建指定大小的随机文件
  - ` fsutil file createnew E:/myfile 1048576000000 `
- 擦除硬盘剩余空间!!!!危险命令!!!!
  - ` cipher /w:E `

## Git Bash 

### 提示符PS1的显示

- 当前目录有变化时,在PS1中显示一个星号
```bash
export GIT_PS1_SHOWDIRTYSTATE=1
```
  - 加入 `~/.bashrc` ， 以如下命令生效`source ~/.bashrc`
### 显示中文乱码
- 在`Git Bash`下，右键 选择 `Options`，选择 `Text` ，将 `Character set` 设置为 `UTF-8`
- 让ls命令能够正常显示中文 `alias ls='ls --show-control-chars --color=auto' `
- 终端中的字符输入输出时不进行转义
```bash
~/.inputrc
set output-meta on
set convert-meta off
```
  - 重新加载 inputrc `bind -f ~/.inputrc`
- less命令的显示
  - ` echo "export LESSHARESET=utf-8" >> ~/.bashrc `
  - ` source ~/.bashrc # 即刻生效配置 `

## 增添常用的Linux命令

大部分的常用命令可以在官网找到 https://www.gnu.org/software/coreutils/ 包括了
- cat: 连接文件并打印内容。
- chgrp: 更改文件的组所有权。
- chmod: 更改文件的权限。
- chown: 更改文件的所有者。
- cp: 复制文件或目录。
- date: 显示或设置系统日期和时间。
- dd: 转换和复制文件，通常用于低级别文件操作。
- df: 显示文件系统磁盘使用情况。
- echo: 显示一段文本或变量的值。
- ln: 创建硬链接或符号链接。
- ls: 列出目录内容。
- mkdir: 创建目录。
- mv: 移动或重命名文件。
- pwd: 显示当前工作目录。
- rm: 删除文件或目录。
- rmdir: 删除空目录。
- touch: 更新文件的时间戳或创建空文件。
- uname: 显示有关操作系统的信息。

除此之外还有一些不包含在内的:
- wget (不含吗? 记忆有些模糊)

这里我们用Windows下的包管理工具来快速安装

## Windows的包安装工具的选择

### Windows 10 

两个主要选择，我们这里以更新，更流行的Scoop为例
- Scoop 
- Chocolatey

```bash
# 通过PowerShell 安装

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
iwr -useb get.scoop.sh | iex
# 上面两行也可以尝试换位 Invoke-WebRequest -Uri 'https://get.scoop.sh' -UseBasicParsing | Iex
scoop install coreutils
```  

### Windows 11 自带了WinGet
```
winget install CoreUtils
```
