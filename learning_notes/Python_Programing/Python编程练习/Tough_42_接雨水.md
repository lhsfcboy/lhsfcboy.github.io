# 接雨水

接雨水问题（Trapping Rain Water Problem）似乎经常出现在国内IT公司的面试环节之中，备受调侃之余，也很值得思考。给定一个非负整数数组 height，数组中的每个元素代表一个柱子的高度。柱子之间的空隙可以接住雨水。你的任务是计算数组中能够接住的雨水的总量。



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