# C语言的消消乐

## 原题地址

https://github.com/csnwc/Exercises-In-C/tree/2d21129e7d4bfec665640720429404bbd2b5531a/Code/Week5/CrushIt

CrushIt.pdf


## 核心功能函数
- 初始化游戏板 (initialise()) - 从文件或给定的字符串初始化游戏板。
- 匹配和清除块 (match()) - 找出水平或垂直线上连续三个或以上相同的块，并将它们替换为'.'（空块）。
- 块的下落 (dropblocks()) - 让块在空的位置下落，直到填满所有的空隙。
- 输出字符串表示 (tostring()) - 将游戏板的当前状态转换为字符串输出。

您需要实现这些功能，而已提供的文件 crushit.c 和 mydefs.h，与 crushit.h 和 driver.c 文件一起，将构成这个游戏的基本框架。您需要完成 crushit.c 中缺失的功能部分。

## 文件和作用

### `crushit.c`
- 作用: 实现游戏逻辑
- 依赖: `crushit.h`, `mydefs.h`

### `crushit.h`
- 作用: 定义函数原型和数据结构
- 依赖: 无

### `mydefs.h`
- 作用: 辅助宏和函数定义
- 依赖: 无

### `driver.c`
- 作用: 程序入口和游戏驱动
- 依赖: `crushit.h`, `mydefs.h`

### `Makefile`
- 作用: 编译和链接规则, 指定编译文件和链接方式


### 文本文件 (`a.txt`, `b1.txt`, `c.txt` 等)
- 作用: 初始化数据

### `ReadMe.pdf`
- 作用: 项目文档
