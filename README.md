# lhsfcboy.github.io
本项目用于创建GitHub的个人主页, 主要是存放些笔记和代码片段~

Quick Note:

```bash

# Install Git Bash
# setup publish SSH key https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh
# setup local commiter information
git config --global user.email "lhsfcboy@gmail.com"
git config --global user.name "Mike Luo"


git clone git@github.com:lhsfcboy/MyFirstGitHub.git
git add  main.c                                            #把文件添加到仓库
git commit -m "add the mail c file "                       #把文件提交到仓库
git push origin master

git fetch                            #先把git的东西fetch到你本地
git merge                            #然后merge后
                                     #这2句命令等价于git pull   
git push                             #再push



#仅获取最新版和一个历史版本,即最后2个版本
git clone git@github.com:nutzam/nutz --depth=1

#压缩空间
git gc --aggressive

#快速指令
git gc

#完全重建版本库
$ rm -rf .git
$ git init
$ git add .
$ git cm "first commit"
$ git remote add origin <your_github_repo_url>
$ git push -f -u origin master
```
