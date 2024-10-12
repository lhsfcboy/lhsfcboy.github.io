## 题目

请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
```
- [73, 74, 75, 71, 69, 72, 76, 73,]
- [ 1,  1,  4,  2,  1,  1,  0,  0,]
```

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

## 分析

两层for循环，把至少需要等待的天数就搜出来了。时间复杂度是O(n^2)。
```python
def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n  # 初始化结果列表
    for i in range(n):
        for j in range(i + 1, n):
            if temperatures[j] > temperatures[i]:
                answer[i] = j - i  # 计算等待天数
                break  # 找到后跳出内层循环
    return answer

# 测试示例
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temperatures))  # 输出：[1, 1, 4, 2, 1, 1, 0, 0]
```


## 本题其实就是找找到一个元素右边第一个比自己大的元素

单调栈通常用于解决这种“下一个更大元素”的问题。
