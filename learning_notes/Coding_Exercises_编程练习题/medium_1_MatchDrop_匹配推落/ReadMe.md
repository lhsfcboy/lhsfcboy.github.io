# ReadMe

## What is good format?

格式要求

- 每个字符大写A-Z
- 第一行是hawk line: 单独字符
- 第二行必须存在
- 第二行长度必须在1到6之间
- 检查第二行之后的所有行
  - 所有第二行之后的行宽度必须等于第二行宽度
  - 最后一行为空行时特殊处理
- 高度检查: 高度不超过6

## How to check if two boards equal?

```text
X
ACC
BBA
CAB
====
X
CAC
BBA
ACB
```

如果我们以char-to-char来判断, 那么以上两个board不一样, 但是如果colmun-to-column来判断, 那么以上两个board是相同的

## If solution exist, what is the max steps?

在当前题目的条件制约(不超过200k/20万的)下, 一个有解的solution最多有多少步?
似乎`20`是个不错的答案.

```text
1.8 ** 20 == 200k
2   ** 18 == 200k
3   ** 12 == 530k
6   ** 12 == 2G   (20亿)
```

Hence, 20 seems to be necessary and long enough for possiable solution, and dint waste too much space.

## How to determine if a solution is possible, and if it is possible, must it necessarily exist?

For a m-column, n-row board, how to determine if a solution is possible?

- Step1, Find & takeout `n` same letters, until not possiable
- Step2, check left letters, if only one, then possiable to solve, else not possialbe.

If we dont have the limitation of 200k boards, it is clear that if the above condations are met, then a solution is possiable and must exist. But could you approve that?

e.g. find a way/steps to solve any possiable solutions.

### 番外篇: 如何计算对数

`2`的`exponent`次方是200k, 那么`exponent`是多少呢?

```text
log2(200k) = log(200k)/log(2)

```

## Test Case

```text
X
AA
BB
AA
BB
AA
BB
==========
X
OU
PV
QW
RX
SY
TZ
```
