## 快速使用

```bash
#仅获取最新版和一个历史版本,即最后2个版本
git clone git@github.com:nutzam/nutz --depth=1
#压缩空间
git gc --aggressive

git add  main.c                                            #把文件添加到仓库
git commit -m "add the mail c file "                       #把文件提交到仓库
git push origin master

git fetch                            #先把git的东西fetch到你本地
git merge                            # merge

git pull                             # 等价于git fetch ; git merge

git push                             #再push

#完全重建版本库
rm -rf .git
git init
git add .
git commit -m "first commit"
git remote add origin git@github.com:lhsfcboy/lhsfcboy.github.io.git
git push -f -u origin master
```

## 基本操作
![image](https://github.com/user-attachments/assets/ebfcb294-4600-4172-966b-03b8ea868f38)

```
git add  main.c                                #把文件添加到仓库
git commit -m "add the mail c file "           #把文件提交到仓库
 
git add -A    # 添加所有改动
git add *     # 添加新建文件和修改，但是不包括删除
git add .     # 添加新建文件和修改，但是不包括删除
git add -u    # 添加修改和删除，但是不包括新建文件
 
git status            # 随时掌握工作区的状态

git diff              # 比较工作区(working directory)与暂存区(stage area)之间的差异
git diff --staged     # 比较暂存区(stage area)与最后一次提交(last commit)之间的差异
git diff --cached     # 与 `--staged` 相同，比较暂存区(stage area)与最后一次提交(last commit)之间的差异
git diff HEAD -- readme.txt # 比较当前 readme.txt 文件在工作区与 HEAD（即最后一次提交）的差异

git reset --hard HEAD^        # HEAD表示当前版本，这个命令使得版本回退到上一个版本，上上一个版本就是HEAD^^
git reset --hard 3628164      # 版本回退到3628164开头的版本
git reflog                    # 用来记录你的每一次命令
```
