# 寻找丑数
Ugly number is a number that only have factors 2, 3 and 5.

## 要求

Design an algorithm to find the nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

## 初学者的样例
```python
def nthUglyNumber(n):
    located_ugly_numbers = set([1,])
    unlocated_ugly_number = set([])
    while n > len(located_ugly_numbers):
        current_max_ugly = max(located_ugly_numbers)
        for i in [current_max_ugly * i for i in (2,3,5)]:
            unlocated_ugly_number.add(i) 
        
        next_ugly_number = min(unlocated_ugly_number)
        unlocated_ugly_number.remove(next_ugly_number)
        located_ugly_numbers.add(next_ugly_number)
        print(located_ugly_numbers)
        print(unlocated_ugly_number)
    return max(located_ugly_numbers)

print(nthUglyNumber(9)    )
```

## ChatGPT样例
```python
import heapq

def nthUglyNumber(n):
    # 初始集合，放入第一个丑数1
    located_ugly_numbers = [1]
    visited = set(located_ugly_numbers)  # 用于存储已经生成过的丑数，防止重复
    factors = [2, 3, 5]  # 因子

    # 创建最小堆
    heap = [1]
    
    # 循环 n 次，直到找到第 n 个丑数
    for i in range(n):
        # 取出堆顶最小的丑数
        current_ugly = heapq.heappop(heap)

        # 遍历因子 2, 3, 5
        for factor in factors:
            new_ugly = current_ugly * factor
            if new_ugly not in visited:  # 避免重复
                visited.add(new_ugly)
                heapq.heappush(heap, new_ugly)

    # 返回第 n 个丑数
    return current_ugly

# 测试
print(nthUglyNumber(9))
```