"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""

class Solution:
    """
    @param: prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # max_profit = 0
        # price_number = len(prices)
        
        # if price_number <= 1:
        #     return 0


            
        # for idx in range(price_number - 1):
        #     following_max_price = max(prices[idx+1:])
        #     profit = following_max_price - prices[idx] 
        #     if profit > max_profit:
        #         max_profit = profit
        # return max_profit
        if len(prices) <= 1:
            return 0
        buy_price = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            buy_price = min(buy_price, prices[i])
            max_profit = max(max_profit, prices[i] - buy_price)
        return max_profit