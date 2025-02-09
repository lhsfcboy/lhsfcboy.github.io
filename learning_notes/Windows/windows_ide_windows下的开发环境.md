# Windows下的开发环境

## WIP win10 配置系统默认utf-8编码

​www.cnblogs.com/walker-world/p/9548852.html

## PowerShell 

### PowerShell 设置 UTF-8 输出编码

要让 PowerShell 的输出编码设置 `[Console]::OutputEncoding = [System.Text.Encoding]::UTF8` 永久生效，需要将其添加到 PowerShell 的配置文件中。具体步骤如下：

```powershell
echo $PROFILE                             # 查看配置文件位置
New-Item -Path $PROFILE -Type File -Force # 创建配置文件（如不存在）
echo $PROFILE      
notepad $PROFILE                          # 编辑配置文件
```

将以下代码添加到配置文件中：
```powershell
# 1. 设置PowerShell控制台的代码页为UTF-8
chcp 65001

# 2. 设置PowerShell的输入输出编码
$OutputEncoding = [System.Text.Encoding]::UTF8
[System.Console]::OutputEncoding = [System.Text.Encoding]::UTF8
[System.Console]::InputEncoding = [System.Text.Encoding]::UTF8

# 3. 为当前用户设置永久性的编码配置
# 检查配置文件是否存在
if (!(Test-Path -Path $PROFILE)) {
    # 如果配置文件不存在，创建配置文件
    New-Item -ItemType File -Path $PROFILE -Force
}

# 添加编码设置到配置文件
$profileContent = @'
# 设置PowerShell的默认编码为UTF-8
$OutputEncoding = [System.Text.Encoding]::UTF8
[System.Console]::OutputEncoding = [System.Text.Encoding]::UTF8
[System.Console]::InputEncoding = [System.Text.Encoding]::UTF8
'@

# 将配置添加到配置文件
Add-Content -Path $PROFILE -Value $profileContent -Force
```

如果遇到执行策略限制，需要运行：
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

完成以上设置后，每次启动 PowerShell 时都会自动使用 UTF-8 编码输出。

--------------------------------------------------------------------------------
## CMD

### 修改输入输出的文件编码为UTF-8.
> chcp 65001
通过如下管理员权限命令使CMD窗口启动时自动使用UTF-8编码(chcp 65001)。
```
reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Command Processor" /v Autorun /t REG_SZ /d "chcp 65001>nul" /f
# 如果需要恢复
reg delete "HKEY_LOCAL_MACHINE\Software\Microsoft\Command Processor" /v Autorun /f
```

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

--------------------------------------------------------------------------------

## 网络传输，SSH远程连接
- 现代的Windows自带SSH命令，已经不需要特意安装下面的终端软件了
  - Putty
- WinSCP

--------------------------------------------------------------------------------

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
