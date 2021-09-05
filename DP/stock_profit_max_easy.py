# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        profit = 0
        if length < 2:
            return profit
        min_price = prices[0]
        for i in range(1, length):
            val = prices[i]
            profit = max(profit, val - min_price)
            min_price = min(val, min_price)
        return profit

def test():
    prices = [7, 1, 5, 3, 6, 4]
    s = Solution()
    ans = s.maxProfit(prices)
    assert ans == 5