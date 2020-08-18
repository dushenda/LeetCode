#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 518. 零钱兑换 II.py
@author     : CALIBRATION
@time       : 2020/8/18 8:51
@description: None
"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]


def main():
    coins = [1, 2, 5]
    amount = 5
    s = Solution()
    res = s.change(amount, coins)
    print(res)


if __name__ == '__main__':
    main()
