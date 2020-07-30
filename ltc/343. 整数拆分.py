#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 343. 整数拆分.py
@author     : CALIBRATION
@time       : 2020/7/30 9:48
@description: None
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[1], dp[2] = 1, 1
        for i in range(3, n + 1):
            for j in range(i - 1, i // 2 - 1, -1):
                dp[i] = max(max(j, dp[j]) * max(i - j, dp[i - j]), dp[i])
        return dp[n]


def main():
    n = 8
    s = Solution()
    res = s.integerBreak(n)
    print(res)


if __name__ == '__main__':
    main()
