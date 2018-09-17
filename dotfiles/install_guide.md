# dotfiles 安装向导

## 下载配置文件

## Linux


## Windows 7 下的 Git Bash

Git Bash 的`ln`命令只会单纯的复制文件.
为了创建软链接, 可以使用`linkd`命令.

[Microsoft Resource Kit Tools](https://www.microsoft.com/en-us/download/details.aspx?id=17657)
在 Win7 及以上的系统中安装会出现不兼容提示，右击选择`兼容性疑难解答` 根据提示选择其实是可以成功安装的。里面包含是很多小工具，我们只需要 linkd.exe 这个。所以在安装按成之后把这个文件复制到你的 path 目录，或者直接把它所在的目录加进 path。

注意, 命令语法是: `linkd symbolfile sourcefile`

```cmd
linkd.exe ~/.bashrc /D/GitHubWorkSpace/lhsfcboy.github.io/dotfiles/.bashrc
linkd.exe ~/.tmux.conf /D/GitHubWorkSpace/lhsfcboy.github.io/dotfiles/.tmux.conf
linkd.exe ~/.vim/vimrc /D/GitHubWorkSpace/lhsfcboy.github.io/dotfiles/vim/vimrc
```
