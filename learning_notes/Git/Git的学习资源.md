# Git的学习资源汇总

## 入门教程
- [git - 简明指南](https://rogerdudler.github.io/git-guide/index.zh.html)
- [廖雪峰 Git教程](https://liaoxuefeng.com/books/git/introduction/index.html)
- 《Git from the inside out 深入浅出 Git》  作者 Mary Rose Cook
  - 原文链接: https://codewords.recurse.com/issues/two/git-from-the-inside-out
  - 作者录制的解释视频：https://www.youtube.com/watch?v=fCtZWGhQBvo
  - 作者用Javascript重现了git http://gitlet.maryrosecook.com/docs/gitlet.html
  - 原作者授权过的中文翻译 https://github.com/pysnow530/git-from-the-inside-out

## 反正也没人看的部分

- [图解Git](http://marklodato.github.io/visual-git-guide/index-zh-cn.html)
- [GotGitHub](http://www.worldhello.net/gotgithub/index.html)
- [Learn Git Branching 小游戏](http://learngitbranching.js.org/)
- [Git 样式指南](https://udacity.github.io/frontend-nanodegree-styleguide-zh/)
- [Git Magic](http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/zh_cn/)
- [Pro Git 中文版](https://git-scm.com/book/zh/v2)
  - 官方出品的 百科全书式的Git介绍
  - [Pro Git 中文版 (备用地址)](https://gitee.com/progit/index.html)
  - 下面是个简约版 [Git核心概念](https://zhuanlan.zhihu.com/p/22750675) 
- [Git分支管理策略 作者： 阮一峰](https://www.ruanyifeng.com/blog/2012/07/git.html)

## Git from the inside out 深入浅出 Git 的读书笔记

- What is the hash value of my file?
`git hash-object data/letter.txt`
 
- What is inside the .git/objects/  BLOB binary large object ?
`git cat-file -p 2e65 #至少要给四个字符作为文件名`
 
- What is in the .git/index ?
```bash
git ls-files --stage
https://stackoverflow.com/questions/4084921/what-does-the-git-index-contain-exactly
$ git ls-files --stage
100644 2e65efe2a145dda7ee51d1741299f848e5bf752e 0   	data/letter.txt
100644 56a6051ca2b02b04ef92d5150c9ef600403cb1de 0   	data/number.txt
```
