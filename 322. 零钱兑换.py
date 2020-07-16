#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 322. 零钱兑换.py
@author     : CALIBRATION
@time       : 2020/7/15 10:41
@description: None
"""


class Solution:
    def coinChange(self, coins: list, amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1 for _ in range(amount + 1)]
        for i in range(1, amount + 1):
            if i in coins:
                dp[i] = 1
                continue
            else:
                tmp = [v for v in coins if v < i]
                cnt = [dp[i - j] + 1 for j in tmp if dp[i - j] != -1]
                if len(cnt) > 0:
                    dp[i] = min(cnt)
        return dp[amount]

    def coinChange2(self, coins: list, amount: int) -> int:
        # 递归
        memo = dict()

        def dp(n):
            if n in memo: return memo[n]
            if n == 0: return 0
            if n < 0: return -1
            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1: continue
                res = min(res, 1 + subproblem)
            memo[n] = res if res != float('INF') else -1
            return memo[n]

        return dp(amount)


def main():
    coins = [2]
    amount = 3
    sol = Solution()
    res = sol.coinChange(coins, amount)
    print(res)


if __name__ == '__main__':
    main()
