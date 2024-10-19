# Bash 的基础操作
- 移动光标
- 命令编辑
- 历史命令

## 移动光标

![快捷键图示](https://raw.githubusercontent.com/fliptheweb/bash-shortcuts-cheat-sheet/master/moving_cli.png)

| 命令      | 描述                                |
|-----------|-------------------------------------|
| ctrl + a  | 跳转到命令行的开头                  |
| ctrl + e  | 跳转到命令行的末尾                  |
| ctrl + b  | 光标向左移动一个字符                |
| ctrl + f  | 光标向右移动一个字符                |
| alt + f   | 光标向右移动一个单词                |
| alt + b   | 光标向左移动一个单词                |

在 Linux 命令行中输入命令时，有许多快捷键，例如 ctrl-a（回到行首）。这些快捷键来自 Readline 行编辑库。
[你可能不知道的 GNU Readline](https://twobithistory.org/2019/08/22/readline.html)

## 编辑/其他操作

| 命令              | 描述                                |
|-------------------|------------------------------------ |
| ctrl + d          | 删除光标下的字符                    |
| ctrl + h          | 删除光标前的字符                    |
| ctrl + u          | 清除光标前的所有内容                |
| ctrl + k          | 清除光标后的所有内容                |
| ctrl + w          | 删除光标前的一个单词                |
| alt + d           | 删除光标后的一个单词                |
| ctrl + y          | 粘贴先前删除的内容                  |
| ctrl + i          | 命令补全（类似 Tab 键）             |
| ctrl + l          | 清屏（等同于 clear 命令）           |
| ctrl + c          | 终止当前运行的进程                  |
| ctrl + d          | 空行发送EOF退出 shell               |
| ctrl + d          | 非空行提交当前输入, 类似Enter       |
| ctrl + z          | 将当前进程置于后台                  |
| alt + [Backspace] | 删除光标前的单词                    |
| alt + ?           | 显示当前路径中的文件/文件夹帮助     |
| alt + *           | 显示当前路径中的所有文件/文件夹     |
| alt + .           | 显示上一个命令的最后一个参数        |
| ~[TAB][TAB]       | 列出所有用户                        |
| $[TAB][TAB]       | 列出所有系统变量                    |
| @[TAB][TAB]       | 列出 /etc/hosts 文件中的所有条目    |
| [TAB]             | 自动补全                            |
| cd -              | 切换到上一个工作目录                |

## 历史记录

| 命令              | 描述                                  |
|-------------------|---------------------------------------|
| ctrl + r          | 从当前行开始，向上搜索历史记录        |
| ctrl + s          | 从当前行开始，向下搜索历史记录        |
| ctrl + p          | 历史记录中的上一条命令, 类似向上箭头）|
| ctrl + n          | 历史记录中的下一条命令, 类似向下箭头）|
| ctrl + o          | 执行通过 Ctrl+r 或 Ctrl+s 搜索到的命令|
| ctrl + g          | 退出历史记录搜索模式                  |
| !!                | 执行上一条命令（如 `sudo !!`）        |
| !vi               | 执行以 vi 开头的上一条命令            |
| !n                | 执行历史记录中的第 n 条命令           |
| !$                | 上一条命令的最后一个参数              |
| !^                | 上一条命令的第一个参数                |
| alt + <           | 跳转到历史记录的第一行                |
| alt + >           | 跳转到历史记录的最后一行              |

### 参考资料
0. https://gist.github.com/tuxfight3r/60051ac67c5f0445efee
1. https://github.com/fliptheweb/bash-shortcuts-cheat-sheet/blob/master/README.md
