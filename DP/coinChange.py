# https://leetcode.com/problems/coin-change/

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        coins.sort(reverse=True)

        exist_amounts = {0}
        current_amounts = [0]
        next_amounts = []

        for coin_number in range(1, amount + 1):
            for one_amount in current_amounts:
                for coin in coins:
                    new_amount = one_amount + coin
                    if new_amount == amount:
                        return coin_number
                    if new_amount in exist_amounts:
                        continue
                    if new_amount < amount:
                        next_amounts.append(new_amount)
                        exist_amounts.add(new_amount)
            current_amounts, next_amounts = next_amounts, []

        return -1

# This is bottom to top solution

    def coinChange2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        _dp = {0: 0}  # {amount: value}

        def dp(n):
            if n < 0:
                return -1
            if n not in _dp:
                candidates = [1 + dp(n - coin) for coin in coins if dp(n - coin) >= 0]  # recursive
                if len(candidates) == 0:
                    _dp[n] = -1
                else:
                    _dp[n] = min(candidates)
            return _dp[n]

        return dp(amount)

# dp(11) = dp(11-5) + 1
#          dp(11-2) + 1
#          dp(11-1) + 1
# This is top to bottom solution

def test():
    s = Solution()
    coins = [1, 2, 5]
    amount = 11
    ans1 = s.coinChange(coins,amount)
    ans2 = s.coinChange2(coins,amount)
    assert ans1 == 3
    assert ans2 == 3