#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


# @lc code=start
import itertools


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_price = prices[0]
        for p in prices:
            min_price = min(p, min_price)
            profit = p - min_price
            result = max(profit, result)
        return result


# @lc code=end
