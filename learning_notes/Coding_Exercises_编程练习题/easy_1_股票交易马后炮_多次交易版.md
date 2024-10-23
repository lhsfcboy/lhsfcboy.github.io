"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

    股票交易问题：
    给定一个数组，其中第i个元素是给定股票第i天的价格。
    
    设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
    
    注意：
    - 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）
    - 每次交易只能买卖一股
    
    示例:
    输入: [7,1,5,3,6,4]
    输出: 7
    解释: 
    - 在第2天（股票价格 = 1）买入，在第3天（股票价格 = 5）卖出, 这笔交易所能获得利润 = 5-1 = 4
    - 在第4天（股票价格 = 3）买入，在第5天（股票价格 = 6）卖出, 这笔交易所能获得利润 = 6-3 = 3
    总利润 = 4 + 3 = 7
    
"""


```python
class Solution:

    
    def maxProfit(self, prices):
        # 处理边界情况
        if len(prices) <= 1:
            return 0
            
        cum_profit = 0
        
        # 遍历价格数组，累加所有上涨区间的利润
        for idx in range(1, len(prices)):
            if prices[idx] > prices[idx - 1]:
                cum_profit += prices[idx] - prices[idx - 1]
        return cum_profit


def run_tests():
    solution = Solution()
    
    # 测试用例1: 有多次交易机会
    test1 = [7,1,5,3,6,4]
    assert solution.maxProfit(test1) == 7, f"Test1 Failed: Expected 7, got {solution.maxProfit(test1)}"
    
    # 测试用例2: 持续下跌，没有交易机会
    test2 = [7,6,4,3,1]
    assert solution.maxProfit(test2) == 0, f"Test2 Failed: Expected 0, got {solution.maxProfit(test2)}"
    
    # 测试用例3: 持续上涨，每天都交易
    test3 = [1,2,3,4,5]
    assert solution.maxProfit(test3) == 4, f"Test3 Failed: Expected 4, got {solution.maxProfit(test3)}"
    
    # 测试用例4: 空数组
    test4 = []
    assert solution.maxProfit(test4) == 0, f"Test4 Failed: Expected 0, got {solution.maxProfit(test4)}"
    
    # 测试用例5: 只有一个价格
    test5 = [1]
    assert solution.maxProfit(test5) == 0, f"Test5 Failed: Expected 0, got {solution.maxProfit(test5)}"
    
    # 测试用例6: 波动价格
    test6 = [1,2,1,2,1,2]
    assert solution.maxProfit(test6) == 3, f"Test6 Failed: Expected 3, got {solution.maxProfit(test6)}"
    
    print("All test cases passed!")

# 运行测试
if __name__ == '__main__':
    run_tests()
```    