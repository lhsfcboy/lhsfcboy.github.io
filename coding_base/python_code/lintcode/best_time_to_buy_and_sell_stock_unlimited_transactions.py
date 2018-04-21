"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""



class Solution:
    """
    @param: prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        
        if len(prices) <= 1:
            return 0
            
        cum_profit = 0
        
        for idx in range(1, len(prices)):
            if prices[idx] > prices[idx -1]:
                cum_profit += prices[idx] - prices[idx -1]
        return cum_profit
            