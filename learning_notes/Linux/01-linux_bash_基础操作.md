# Bash 的基础操作

## 移动光标

![快捷键图示](https://raw.githubusercontent.com/fliptheweb/bash-shortcuts-cheat-sheet/master/moving_cli.png)

| 命令      | 描述                                |
|-----------|-------------------------------------|
| ctrl + a  | 跳转到命令行的开头                   |
| ctrl + e  | 跳转到命令行的末尾                   |
| ctrl + b  | 光标向左移动一个字符                 |
| ctrl + f  | 光标向右移动一个字符                 |
| alt + f   | 光标向右移动一个单词                 |
| alt + b   | 光标向左移动一个单词                 |
| ctrl + xx | 在行首与当前光标位置之间切换         |
| ctrl + ] + x | 光标跳转到下一个 x 字符的出现位置 |
| alt + ctrl + ] + x | 光标跳转到上一个 x 字符的出现位置 |

在 Linux 命令行中输入命令时，有许多快捷键，例如 ctrl-a（回到行首）。这些快捷键来自 Readline 行编辑库。
[你可能不知道的 GNU Readline](https://twobithistory.org/2019/08/22/readline.html)

## 编辑/其他操作

| 命令              | 描述                                |
|-------------------|-------------------------------------|
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
| ctrl + d          | 退出 shell（当行为空时与 exit 命令相同） |
| ctrl + z          | 将当前进程置于后台                  |
| ctrl + _          | 撤销                               |
| ctrl + x ctrl + u | 撤销上一次更改，等同于 ctrl + _     |
| ctrl + t          | 交换光标前的两个字符                |
| esc + t           | 交换光标前的两个单词                |
| alt + t           | 交换当前单词与前一个单词           |
| esc + .           |                                    |
| esc + _           |                                    |
| alt + [Backspace] | 删除光标前的单词                   |
| alt + <           | 跳转到历史记录的第一行              |
| alt + >           | 跳转到历史记录的最后一行            |
| alt + ?           | 显示当前路径中的文件/文件夹帮助     |
| alt + *           | 显示当前路径中的所有文件/文件夹     |
| alt + .           | 显示上一个命令的最后一个参数        |
| alt + c           | 将单词从光标处开始大写              |
| alt + u           | 将单词从光标处开始转换为大写        |
| alt + l           | 将单词从光标处开始转换为小写        |
| alt + n           |                                    |
| alt + p           | 非增量反向搜索历史记录              |
| alt + r           | 撤销对当前行的所有更改              |
| alt + ctrl + e    | 扩展命令行                         |
| ~[TAB][TAB]       | 列出所有用户                       |
| $[TAB][TAB]       | 列出所有系统变量                   |
| @[TAB][TAB]       | 列出 /etc/hosts 文件中的所有条目    |
| [TAB]             | 自动补全                           |
| cd -              | 切换到上一个工作目录               |

## 历史记录

| 命令              | 描述                                |
|-------------------|-------------------------------------|
| ctrl + r          | 从当前行开始，向上搜索历史记录       |
| ctrl + s          | 从当前行开始，向下搜索历史记录       |
| ctrl + p          | 获取历史记录中的上一条命令（等同于向上箭头） |
| ctrl + n          | 获取历史记录中的下一条命令（等同于向下箭头） |
| ctrl + o          | 执行通过 Ctrl+r 或 Ctrl+s 搜索到的命令 |
| ctrl + g          | 退出历史记录搜索模式                |
| !!                | 执行上一条命令（如 `sudo !!`）      |
| !vi               | 执行以 vi 开头的上一条命令          |
| !vi:p             | 打印以 vi 开头的上一条命令          |
| !n                | 执行历史记录中的第 n 条命令         |
| !$                | 上一条命令的最后一个参数            |
| !^                | 上一条命令的第一个参数              |
| ^abc^xyz          | 将上一条命令中的 abc 替换为 xyz 并执行 |

---

### 参考资料
0. https://gist.github.com/tuxfight3r/60051ac67c5f0445efee
1. https://github.com/fliptheweb/bash-shortcuts-cheat-sheet/blob/master/README.md
