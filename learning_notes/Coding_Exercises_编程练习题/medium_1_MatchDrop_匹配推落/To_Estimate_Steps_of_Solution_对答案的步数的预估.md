# To Estimate Steps of Solution

在完成Week8 Assignment时, 我在`mydefs.h`中定义了如下一个常数.

```c
#define CNT_LS_LEN 20
```

这篇文章解释了我是如何决定这个具体的常数的值.

## 问题的背景与产生

![alt text](树状图_JPEG格式.jpg)

在解决Match Drop问题时, 我们实质上生成了一颗树状结构, 其中每个节点代表board的一种状态.
每个节点还都保存了指向parent_board的指针.

在实现solve函数中的verbose 功能的过程中. 需要依次打印出从0开始到第一个找到的解的棋盘状态.
e.g. In above diagram, the first found solved board is `board_id:105`, and then we use parent_id reference to find the trail: `[0,2,5, ...... , 105]`
因此, 需要有一个数组来储存这一系列的棋盘的`board_id`.
And in above case, the array size is `N + 1`.

And for the very first step, I need to decide the size of the array.
Since `-Wvla` is used in the given Makefile, I cant use the feature of `Variable Length Arrays` to detamine the array size when running the code.
Insted, I have to datemine the size of the array during comipler phase.

Hence, I realized that I need to find a reasonable upper limit for the array size.
It should be long enough to store the trail, but not waste too much memory space.
Apprantely, the upper limit is definately lower then 200,000.
But could we reduce it further?

Appearently, this value is only rquired when we do have a solution.

- The board have no solution.
- The board have a solution, but the first solution is beyond 200,000. In our case, this is consider as `not resovlable`
- The board have a solution, and the first solution is lower then 200,000.

### 其他的可能的解决办法

使用动态内存分配可以避免VLA的警告.

```c
int n = 10;
int *array = malloc(n * sizeof(int));
free(array);
```

但是在这个具体的题目下, 我非常好奇能否合理的预估出最终的solution_steps的大小.

## 符号和概念的定义

BRDSZ: definition…
MAXBRDS:  definition…
CNT_LS_LEN:  definition…        // 变量名备选: solution_size  solution_steps solution_list
n: generation_num
generation：definition…

## 具体的数学推导/展示计算过程

As a beginning, I started with the most complated case: a 6 * 6 board.



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
其中的公式部分使用了https://www.sciweavers.org/free-online-latex-equation-editor来生成基于LaTex语法的方程式图片.
图片部分使用了Google Drawings.
请问老师在具体工具上有哪些推荐?
