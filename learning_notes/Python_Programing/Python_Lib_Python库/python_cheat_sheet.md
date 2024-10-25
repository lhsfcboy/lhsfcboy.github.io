# python 备忘录

## 数值计算

- 求列表的平均值

```python
sum(l)/len(l)
import numpy as np
print np.mean(l)
```

- 获取两数相除的商和余数

```python
div, mod = divmod(a, b)
div = a // b
mod = a % b
```

## 字符串处理

- 使用多个字符对string进行分隔

```python
import re
re.split("[,. ]", "this is.a,test ")
# 注意, 中括号里有个空格
```

- 大小写,首字母大写

```python
print(str.upper())          # 把所有字符中的小写字母转换成大写字母
print(str.lower())          # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写
```