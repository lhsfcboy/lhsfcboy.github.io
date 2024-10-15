# for 循环中判断是否是最后一个元素

- [What is the pythonic way to detect the last element in a 'for' loop?](https://stackoverflow.com/questions/1630320/what-is-the-pythonic-way-to-detect-the-last-element-in-a-for-loop/1630350)

## 参考实现
```python
def lookahead(iterable):
    """遍历给定的可迭代对象，增加是否有后续值的信息。
    如果当前值后还有更多值，则标记为 True；
    如果是最后一个值，则标记为 False。
    """
    count = 0
    # 获取迭代器并取出第一个值
    it = iter(iterable)
    last = next(it)
    # 从第二个值开始遍历迭代器直到结束
    for val in it:
        # 报告前一个值（还有更多值）
        count += 1
        yield count, last, True
        last = val
    # 报告最后一个值
    count += 1
    yield count, last, False

for i, line, has_more in lookahead(range(3)):
    print(i, line, has_more)
```
