#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 647. 回文子串.py
@author     : CALIBRATION
@time       : 2020/8/19 8:46
@description: None
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        # 暴力法
        res = 0
        for a in range(len(s)):
            for b in range(a + 1, len(s) + 1):
                tmp = s[a:b]
                if tmp == tmp[::-1]:
                    res += 1
        return res

    def countSubstrings2(self, s: str) -> int:
        # 动态规划
        dp = [[False] * len(s)] * len(s)
        res = 0
        for i in range(len(s)):
            dp[i][i] = True
            res += 1
        for i in range(len(s)):
            for j in range(i + 2, len(s) + 1):
                tmp = s[i:j]
                if dp[i][j - 1] and tmp == tmp[::-1]:
                    res += 1
        return res

    def countSubstrings3(self, s: str) -> int:
        pass


def main():
    s = Solution()
    res = s.countSubstrings2("abc")
    print(res)


if __name__ == '__main__':
    main()
