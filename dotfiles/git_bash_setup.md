ls ~/.bash_profile


alias gs="git status"

alias ls='ls --show-control-chars'    # 避免日语乱码


Git for Windows のインストーラでそのまま入れると大体は"C:\Program Files(x86)\Git\bin\"にある"vim"を編集します。


vim ~/.gitconfig

[core]
        editor = /C/vim/gvim --nofork -c 'set fenc=utf-8' +1
        
        
### 修改GitBash的提示符(prompt)

使用管理员权限修改文件: `C:\Program Files\Git\etc\profile.d\git-prompt.sh`

### 解决git status不能显示中文

status查看有改动但未提交的文件时总只显示数字串，显示不出中文文件名，在默认设置下，中文文件名在工作区状态输出，中文名不能正确显示，而是显示为八进制的字符编码。

将git 配置文件 core.quotepath项设置为false。quotepath表示引用路径, 加上--global表示全局配置.

git bash 终端输入命令：`git config --global core.quotepath false`

### 解决git bash 终端显示中文乱码

git bash终端也要设置成中文和utf-8编码, 才能正确显示中文.
git bash的界面中右击空白处，弹出菜单，选择`选项->文本->本地Locale`，设置为`zh_CN`，而旁边的字符集选框选为`UTF-8`

###### 还可以通过直接修改配置文件的方式来解决中文乱码问题
编辑etc\gitconfig文件，也有些windows系统是存放在C:\Users\Administrator\.gitconfig路径或安装盘符:\Git\mingw64\etc\gitconfig，在文件末尾增加以下内容：

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
