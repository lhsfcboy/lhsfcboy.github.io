# 理想的记录笔记的方式
在哪里发布我刚编的故事：

有些问题反复思考，落实到纸面的内容才

输出会强迫更加有深度的思考，

## 个人建站 vs 使用博客平台

定期备份内容

第三方风险：平台基于第三方的政治商业压力对内容的管控，特别是无预警删帖。

存在内容被封禁删除的风险
使用脚本定期备份？
避免灰色内容的题材

## 博客平台的选择

在经常访问的地方

有持续的高质量内容的，互动质量比较高

知乎/B站/小红书

小红书无法创作深度内容，只适合短篇分享

B站整体是一个视频网站，

## Github Issues 作为博客？

## 有关Markdown
Markdown格式虽然简洁，但是仅适合纯文字的内容。图片需要另外储存。使用第三方图床则给自己引入了不必要的外部依赖。使用自己的GitHub作为图床，目录管理又太复杂。

## 摸鱼
创作博客的最佳时间莫过于上班时了！

最近公司封禁了个人账户登录GitHub，所以可以放弃了。



## 网络内容的引用
链接是极度不可靠的，十年前的笔记中所引用的链接已经大部分失效。
主要内容还是要全文引用。

## MS OneNote
Pros
- 格式丰富

Cons
- 格式调整复杂，难以控制
- 国内同步慢

## 有道云笔记

Pros
- 支持markdown格式
- 国内同步快

Cons
- 发生过同步错误的问题

## 知乎
Pros
- 高质量内容多
- 公司内可以访问
- 支持一定程度的Latex功能
  - 手机端显示有问题

Cons
- 表格功能孱弱
  - 可以借助Latex实现
- 所有外站链接都需要额外跳转
- 图片功能比较孱弱
  - 没有任何的简单编辑功能, 例如大小调整
  - 可以借助第三方的在线的`图片resize`服务
    - https://picresize.com/
    - https://www.adobe.com/express/feature/image/resize
    - https://imageresizer.com/
  - 如果主要使用来自网络的图片, 还可以考虑Chrome插件的形式调整图片大小
## GitHub Markdown
  - 键盘快捷键直观且方便
    - e 编辑
    - Ctrl S 保存  Enter 确认
  - GitHub的Web版本下，Markdown可以自动处理图片了！
    - Markdown的图片管理曾经是个非常头疼的问题，现在竟然有了免费的图床!
    - 可以在Markdown中储存不够重要的图片
## Github Jupyter
- 似乎不支持raw类型的cell的web显示, 需要用Markdown格式的cell保存说明文字的cell
## 本地MarkDown

每篇文章独立一个文件夹.
- 方便管理
- 阅读不便
```text
    blog/
        ├─ 数据,信息,知识,智慧/
        │   ├── data
        │   │   └── 2000.csv
        │   ├── images
        │   │   ├── 1.png
        │   │   └── 2.jpg
        │   └── readme.md
        └─ 中心极限定理的直观理解/
            ├── data
            │   └── 2000.csv
            ├── images
            │   ├── 1.png
            │   └── 2.jpg
            └── readme.md
```

所有文章公用一个图片文件夹
- 图片不容易管理
- 适合系列文章
```text
    blog/
        ├─ 数据,信息,知识,智慧.md
        ├── 中心极限定理的直观理解.md
        ├── data
        │   └── 2000.csv
        └── images
            ├── 1.png
            └── 2.jpg
```

所有文章有一个同名的文件夹     
```text
    blog/
        ├─ 数据,信息,知识,智慧.md
        ├─ 数据,信息,知识,智慧/
        │   ├── data
        │   │   └── 2000.csv
        │   ├── images
        │   │   ├── 1.png
        │   │   └── 2.jpg
        │   └── readme.md
        └─ 中心极限定理的直观理解.md  
        └─ 中心极限定理的直观理解/
            ├── data
            │   └── 2000.csv
            ├── images
            │   ├── 1.png
            │   └── 2.jpg
            └── readme.md
```


## 个人知识库

- 博客
- 笔记
- 代码
- 备忘录
- TODO

## 网络足迹
有任何的主动输入，上传，点赞，收藏的网站均可被视为存在网络足迹。
仅浏览的网站则不论。

谷歌系

百度系


独立系

豆瓣：影音记录


## 有关博客的选择

- 完全的自主性
- 不受审查
- 管理成本低
- 博客vs非公开
  - 低质量的评论难以限制  
  
## 笔记软件

自己搭建平台管理太复杂

## 网盘

## 目前的想法

减少本地文件数量。

- Dropbox
  - 免费版，容量20G
  - 存放不需要变化，但经常使用的
- 百度网盘
  - 免费版，容量2000G
  - 存放可以丢失的文件
- 百度出品的一刻相册 & 夸克网盘
  - 文件临时周转
- 谷歌云端硬盘
  - 免费版，容量20G，容量与谷歌邮箱共用
  - Google Apps Script功能强大
  - Google Colab 使用方便
  - 国内访问困难
  - 手机端编辑困难
- 知乎博客
  - 上班时间写下博客
- GitHub
  - 上班时间看看代码，目前已经无法登录私人账号了
  - GitHub的Web版本下，Markdown可以自动处理图片了！
    - Markdown的图片管理曾经是个非常头疼的问题，现在竟然有了免费的图床!
- WorkFlowy
  -  纯文字笔记
准备废弃的工具：不再增添新内容，逐步转移，准备退役
- MS OneNote
- 有道云笔记
  - 发生过一次笔记丢失问题
  - 限定同步设备只有两台
- 本地磁盘
- [GitHub Gist](https://gist.github.com/lhsfcboy/)

需要定期检查清理

- Google云盘中 表格文件里的TODO
- 手机的备忘录
- 手机的照片
- 微信聊天记录
- 谷歌日历上以安排但是未处理的日程
- Youtube的收藏夹&稍后看
- Bilibili的收藏夹&稍后看
- 知乎的点赞记录，已发表文章，文章草稿
- 小红书的点赞与收藏
- DropBox的代办文件夹
- 电子邮箱中未处理的邮件
- SNS平台
  - Instagram
  - Twitter
  - 知乎
  - 微博
  - Youtube
  - Facebook
  - LinkedIn
