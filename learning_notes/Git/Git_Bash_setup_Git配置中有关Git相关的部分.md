# Git Bash 的安装与配置

## Git配置SSH连接

[通过 SSH 连接到 GitHub](https://docs.github.com/zh/authentication/connecting-to-github-with-ssh)
```bash
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
## 找到Git的本地配置文件

```bash
        ## 查看不同级别的配置以及文件文件
        git config --system --list --show-origin # 系统级别
        git config --global --list --show-origin # 用户级别
        git config --local --list --show-origin  # Git项目内的项目级别配置以及配置文件路径
        # 查看当前生效的配置以及路径
        git config --list --show-origin
```

## Git的本地配置内容

```bash
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

# 解决中文显示问题
git config --global i18n.commitencoding utf-8    # 设置 Git 的 commit message 编码
git config --global i18n.logoutputencoding utf-8 # 设置 Git 日志输出的编码
git config --global core.pathnameencoding utf-8  # 设置 Git 文件路径名编码
git config --global core.quotepath false         # 关闭对非 ASCII 字符的转义
# 输出文件路径时，是否对非 ASCII 字符进行引号和转义编码的设置


# 检查当前的配置情况
git config --list --show-origin
```
