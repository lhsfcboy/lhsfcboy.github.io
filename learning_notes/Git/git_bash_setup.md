# Git Bash 的安装与配置

## Git配置SSH连接
```bash
# setup publish SSH key https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh
# Git配置SSH-Key
ls ~/.ssh
cat ~/.ssh/id_rsa.pub
# 再打开你的github，进入配置页： Settings -- SSH and GPG keys
# 添加本地生成的ssh秘钥，选择New SSH key（这里已经配置了一个key，如果是未配置秘钥的用户，这里是空的）：
# 如果本地网络封锁了SSH默认端口，还可以尝试用443
# https://docs.github.com/en/authentication/troubleshooting-ssh/using-ssh-over-the-https-port

# 测试是否配置成功
ssh -T git@github.com 
# Hi (username)! You've successfully authenticated, but GitHub does not provide shell access.
```

另外一种临时的办法是使用token，但是有效期最长只能设置为一年， 
```
git config --global github.token yourtoken
```


## Git的本地配置

```bash
# setup local commiter information
# 在config里面配置github.com里的用户名和邮箱

git config --global user.email  "lhsfcboy@gmail.com"
git config --global user.name   "Mike Luo"
git config --global color.ui    true

# 常用的命令缩写

git config --global alias.st status        # 通过 git st的形式来使用
git config --global alias.co checkout 
git config --global alias.ci commit
git config --global alias.br branch
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
git config --global alias.unstage 'reset HEAD'
git config --global alias.last    'log -1'

git config --list --global
```
.git/config    	每个仓库的Git配置文件
.gitconfig 	当前用户的Git配置文件放在用户主目录下

## 避免文件乱码

```bash
ls ~/.bash_profile

alias gs="git status"
alias ls='ls --show-control-chars'    # 避免日语乱码

vim ~/.gitconfig

[core]
        editor = /C/vim/gvim --nofork -c 'set fenc=utf-8' +1
```        
        
## 修改GitBash的提示符(prompt)

使用管理员权限修改文件: `C:\Program Files\Git\etc\profile.d\git-prompt.sh`

## 解决git status不能显示中文

status查看有改动但未提交的文件时总只显示数字串，显示不出中文文件名，在默认设置下，中文文件名在工作区状态输出，中文名不能正确显示，而是显示为八进制的字符编码。

将git 配置文件 core.quotepath项设置为false。quotepath表示引用路径, 加上--global表示全局配置.

git bash 终端输入命令：`git config --global core.quotepath false`

## 解决git bash 终端显示中文乱码

git bash终端也要设置成中文和utf-8编码, 才能正确显示中文.
git bash的界面中右击空白处，弹出菜单，选择`选项->文本->本地Locale`，设置为`zh_CN`，而旁边的字符集选框选为`UTF-8`

###### 还可以通过直接修改配置文件的方式来解决中文乱码问题

编辑etc\gitconfig文件，也有些windows系统是存放在`C:\Users\Administrator\.gitconfig`路径或`安装盘符:\Git\mingw64\etc\gitconfig`，在文件末尾增加以下内容：

```
[gui]  
    encoding = utf-8  
    # 代码库统一使用utf-8  
[i18n]  
    commitencoding = utf-8  
    # log编码  
[svn]  
    pathnameencoding = utf-8  
    # 支持中文路径  
[core]
    quotepath = false 
    # status引用路径不再是八进制（反过来说就是允许显示中文了）
```

编辑etc\git-completion.bash文件,在文件末尾增加以下内容：
```
# 让ls命令能够正常显示中文
alias ls='ls --show-control-chars --color=auto' 
```

编辑etc\inputrc文件，修改output-meta和convert-meta属性值：
```
set output-meta on  # bash可以正常输入中文  
set convert-meta off  
```
编辑profile文件，在文件末尾添加如下内容：
```
export LESSHARESET=utf-8
```

## GitBash 使用的其他技巧
- 快速编辑模式：在Bash窗口上点右键 选择Properties，选中QuiteEditMode
  - 启用快速编辑模式后，可以直接在 Git Bash 窗口中通过鼠标右键来复制和粘贴文本
  - 选择文本：你可以通过左键单击并拖动鼠标来选择文本，松开鼠标后，选择的文本会自动复制到剪贴板
  - 粘贴文本：右键单击 Bash 窗口，将剪贴板中的内容粘贴到当前光标位置。
- 同样的位置设置插入模式InsertMode复选框勾上
  - 插入模式下，输入的文本将插入到当前光标所在位置，而不会替换光标后的文本
