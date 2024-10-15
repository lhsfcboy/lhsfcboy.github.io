# 连续标签数据汇总

编写一个函数，该函数接受一个包含元组的列表作为输入。每个元组包含两个元素：一个字符串（标签）和一个整数（值）。函数的目的是对连续的相同标签的整数值进行累加汇总。

## 输入格式
输入是一个元组列表，元组由一个字符串和一个整数组成，例如：
```python
data = [
    ('A', 1),
    ('A', 2),
    ('A', 3),
    ('B', 1),
    ('A', 1)
]
```
可能为空

## 输出格式
输出也应该是一个元组列表，但每个连续的相同标签只出现一次，并且其整数值是该标签连续出现时所有整数的总和。例如，对于上述输入，正确的输出应该是：
```python
[('A', 6), ('B', 1), ('A', 1)]
```

## 任务
实现一个名为 summarize_data 的函数，该函数接收上述描述的输入格式，并返回相应的汇总输出。

## 参考

```python
def summarize_data(data):
    result = []
    if not data:
        return result
    
    current_label = data[0][0]
    current_sum = data[0][1]
    
    for label, value in data[1:]:
        if label == current_label:
            current_sum += value
        else:
            result.append((current_label, current_sum))
            current_label = label
            current_sum = value
    
    result.append((current_label, current_sum))
    
    return result

def test_summarize_data():
    assert summarize_data([]) == [], "Test Case 1 Failed: Empty data should return empty list"
    assert summarize_data([('A', 1)]) == [('A', 1)], "Test Case 2 Failed: Single data point"
    assert summarize_data([('A', 1), ('B', 2), ('C', 3)]) == [('A', 1), ('B', 2), ('C', 3)], "Test Case 3 Failed: No consecutive duplicates"
    assert summarize_data([('A', 1), ('A', 2), ('A', 3)]) == [('A', 6)], "Test Case 4 Failed: All same label"
    assert summarize_data([('A', 1), ('A', 2), ('B', 1), ('A', 1)]) == [('A', 3), ('B', 1), ('A', 1)], "Test Case 5 Failed: Consecutive duplicates mixed with single occurrences"
    assert summarize_data([('A', 1), ('A', 2), ('A', 3), ('B', 1)]) == [('A', 6), ('B', 1)], "Test Case 6 Failed: Consecutive duplicates ending with a different label"
    assert summarize_data([('A', 1), ('A', 2), ('B', 1), ('B', 1), ('C', 1), ('A', 1), ('A', 1)]) == [('A', 3), ('B', 2), ('C', 1), ('A', 2)], "Test Case 7 Failed: Long list with various patterns"
    assert summarize_data([('A', 1), ('B', 1), ('B', 2), ('C', 1), ('A', 2), ('A', 1)]) == [('A', 1), ('B', 3), ('C', 1), ('A', 3)], "Test Case 8 Failed: Changing patterns"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_summarize_data()
```
