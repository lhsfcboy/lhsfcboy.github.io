# 接雨水

接雨水问题（Trapping Rain Water Problem）似乎经常出现在国内IT公司的面试环节之中，备受调侃之余，也很值得思考。

给定一个非负整数数组 height，数组中的每个元素代表一个柱子的高度。柱子之间的空隙可以接住雨水。你的任务是计算数组中能够接住的雨水的总量。

参考资料
- [【力扣hot100】【LeetCode 42】接雨水｜双指针](https://www.bilibili.com/video/BV1CmtZePErE/)
- [Python|动态规划解接雨水问题](https://developer.aliyun.com/article/1257648)
- https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0042.接雨水.md

## 理解题意

显然，最左侧和最右侧的柱子是不会接到雨水的
```
接雨水以前
|                     *  
|         *           *  *     *
|   *     *  *     *  *  *  *  *  *
+-----------------------------------
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] << 柱子高度

接雨水以后
|                     *  
|         *  ^  ^  ^  *  *  ^  *
|   *  ^  *  *  ^  *  *  *  *  *  *
+-----------------------------------
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] << 柱子高度
[0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0] << 雨水高度
```


## Solve it straight-forward

| h    | 0 | 1 | 0 | 2 | 1 | 0 | 1 | 3 | 2 | 1 | 2 | 1 |
|------|---|---|---|---|---|---|---|---|---|---|---|---|
| maxL | 0 | 0 | 1 | 1 | 2 | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 
| maxR | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 1 | 0 |
| min  | 0 | 0 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 0 |
| rain | 0 | 0 | 1 | 0 | 1 | 2 | 1 | 0 | 0 | 1 | 0 | 0 |

注意观察，每个柱子左侧的最高

```Python
def trap(height):
     ans = 0
     for i in range(len(height)):
         max_left, max_right = 0, 0

         # 寻找 max_left
         for j in range(0, i):
            max_left = max(max_left,  height[j])

         # 寻找 max_right
         for j in range(i, len(height)):
            max_right = max(max_right,  height[j])

         if min(max_left, max_right) > height[i]:
            ans += min(max_left, max_right) -  height[i]

     return ans

height=[0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
```


## 思路升级版 双指针
```python
import unittest
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        result = 0
        max_v = max(height)
        max_index = height.index(max_v)
        i = 0
        j = len(height) - 1
        last = 0
        while i < max_index:
            if height[i] > last:
                last = height[i]
            elif height[i] < last:
                result += (last - height[i])
            i += 1
        last = 0
        while j > max_index:
            if height[j] > last:
                last = height[j]
            elif height[j] < last:
                result += (last - height[j])
            j -= 1
        return result

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_trap(self):
        # 测试用例1：空列表
        self.assertEqual(self.solution.trap([]), 0)
        
        # 测试用例2：没有储水的情况（递增）
        self.assertEqual(self.solution.trap([1, 2, 3, 4]), 0)
        
        # 测试用例3：没有储水的情况（递减）
        self.assertEqual(self.solution.trap([4, 3, 2, 1]), 0)
        
        # 测试用例4：正常储水情况
        self.assertEqual(self.solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
        
        # 测试用例5：所有柱子高度相同
        self.assertEqual(self.solution.trap([3, 3, 3, 3]), 0)
        
        # 测试用例6：单个柱子
        self.assertEqual(self.solution.trap([1]), 0)
        
        # 测试用例7：两个柱子
        self.assertEqual(self.solution.trap([1, 2]), 0)

if __name__ == "__main__":
    unittest.main()
```    