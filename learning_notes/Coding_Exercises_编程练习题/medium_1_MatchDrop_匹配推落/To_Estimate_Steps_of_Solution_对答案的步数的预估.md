# To Estimate Steps of Solution

在完成Week8 Assignment时, 我在`mydefs.h`中定义了如下一个常数.

```c
#define CNT_LS_LEN 20
```

这篇文章解释了我是如何决定这个具体的常数的值.

## 问题的背景与产生
![alt text](树状图_JPEG格式.jpg)
在实现solve函数中的verbose 功能的过程中. 需要依次打印出从0开始到第一个找到的解的棋盘状态.
因此, 需要有一个数组来储存这一系列的棋盘的.

Since `-Wvla` is used in the given Makefile, I cant use the feature of `Variable Length Arrays` to detamine the array size when running the code.
Insted, I have to datemine the size of the array during comipler phase.

需要list
c99同意了c11又不允许的变量长数组
变长数组
solution_steps 的数组的长度需要pre-define
lower limit,  upper limit <== 上限有一个合理的估计
uppler limit <= MAXBRDS(200k)
long enough but dont waste to much memory space

## 符号和概念的定义

BRDSZ: definition…
MAXBRDS:  definition…
CNT_LS_LEN:  definition…        // 变量名备选: solution_size  solution_steps solution_list
n: generation_num
generation：definition…

## 具体的数学推导/展示计算过程

most complex case  6*6 ,   ==>   可能的steps
width matters,
all possiable 排列   vs   MAXBRDS
6 ===>  5  , 4, ,3,2
前提条件是有解:
all possiable 排列   <=  MAXBRDS
all possiable 排列   >   MAXBRDS
排除了
无解
有解 但是第一个解在MAXBRDS以后
罗列计算公式等

## 结语

## 后记

这份文件是用Markdown格式编写以后转换为PDF格式的.
其中的公式部分使用了LaTex 公式编辑器语法.
图片部分使用了Google Drawings.
请问老师在具体工具上有哪些推荐?
