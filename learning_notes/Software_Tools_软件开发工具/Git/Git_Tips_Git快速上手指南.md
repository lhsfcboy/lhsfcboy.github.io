## 常用命令

- [常用 Git 命令清单](https://www.ruanyifeng.com/blog/2015/12/git-cheat-sheet.html)

## 快速使用

```bash
####远程拉取####
#仅获取最新版和一个历史版本,即最后2个版本
git clone git@github.com:nutzam/nutz --depth=1
#压缩空间
git gc --aggressive

####本体修改并push#####
git add  main.c                                            #把文件添加到仓库
git commit -m "add the mail c file "                       #把文件提交到仓库
git push origin master

####与远程保持同步#####
git fetch                            #把git的东西抓取到你本地
git merge                            # 再merge

git pull                             # 等价于git fetch ; git merge

git push                             #再push

####完全重建版本库####危险!!!!#####
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

## Git使用技巧

### 永久删除文件(包括历史记录)
 
- https://rtyley.github.io/bfg-repo-cleaner/
- https://stackoverflow.com/questions/2100907/how-to-remove-delete-a-large-file-from-commit-history-in-git-repository
 
Github官方指南
- https://help.github.com/articles/removing-files-from-a-repository-s-history/
- https://help.github.com/articles/removing-sensitive-data-from-a-repository/
 
### Git管理空目录
 
Git仅跟踪文件的变动，不跟踪目录。变通的解决办法是在空目录下存一个 .gitignore 文件。然后 git add 。

如果有许多这样的空目录，可以用下面的命令自动补充 .gitignore 文件：
`$ find . \( -type d -empty \) -and \( -not -regex ./\.git.* \) -exec touch {}/.gitignore \;`

递归找寻当前目录下，类型为目录，且为空，也没有 .git 开头的文件，在其中用 touch 新建一个空的 .gitignore 文件。然后 git add . 之后即可。
