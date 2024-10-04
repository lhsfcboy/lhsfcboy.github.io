# Windows下的开发环境

## Git Bash 的安装

## Git Bash 的基础配置
- 快速编辑模式：在Bash窗口上点右键 选择Properties，选中QuiteEditMode
  - 启用快速编辑模式后，可以直接在 Git Bash 窗口中通过鼠标右键来复制和粘贴文本
  - 选择文本：你可以通过左键单击并拖动鼠标来选择文本，松开鼠标后，选择的文本会自动复制到剪贴板
  - 粘贴文本：右键单击 Bash 窗口，将剪贴板中的内容粘贴到当前光标位置。
- 同样的位置设置插入模式InsertMode复选框勾上
  - 插入模式下，输入的文本将插入到当前光标所在位置，而不会替换光标后的文本

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
