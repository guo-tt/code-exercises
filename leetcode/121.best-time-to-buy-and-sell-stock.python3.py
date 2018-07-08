#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (43.60%)
# Total Accepted:    314.4K
# Total Submissions: 721K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# If you were only permitted to complete at most one transaction (i.e., buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.
# 
# Note that you cannot sell a stock before you buy one.
# 
# Example 1:
# 
# 
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
# 
# 
# Example 2:
# 
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
# 
#
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # thismax = 0
        # max = 0
        # i = 0
        # n = 1
        # k = 1
        # while i < len(prices): 
        #     if i + 1 < len(prices):
        #         for k in range(i+1,len(prices)):
        #             thismax = prices[k] - prices[i]
        #             if thismax < 0:
        #                 thismax = 0 
        #             if thismax > max:
        #                 max = thismax
        #     i += 1
        minVal = 10000000000
        maxGain = 0
        Gain = 0

        for i in range(0,len(prices)):
            Gain = prices[i] - minVal

            if prices[i] < minVal:
                minVal = prices[i]
            if Gain > maxGain:
                maxGain = Gain
        return maxGain

print(Solution().maxProfit([1,2,3,4,5]))
        
