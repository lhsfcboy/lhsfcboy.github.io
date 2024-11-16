# To Estimate Steps of Solution

## 问题的背景与产生
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
