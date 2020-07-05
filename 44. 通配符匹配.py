#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 44. 通配符匹配.py
@author     : CALIBRATION
@time       : 2020/7/5 14:54
@description: None
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # m->s,n->p
        m, n = len(s) + 1, len(p) + 1
        dp = [[False for _ in range(m)] for _ in range(n)]  # n*m

        dp[0][0] = True
        # *开头的问题
        for i in range(1, n):
            if p[i - 1] == "*":
                dp[i][0] = True
            else:
                break
        # pi,sj
        for i in range(1, n):
            for j in range(1, m):
                # 状态转移方程
                if p[i-1] == s[j-1] or p[i-1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                if p[i-1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[n-1][m-1]


def main():
    sol = Solution()
    s = "aa"
    p = "a"
    res = sol.isMatch(s, p)
    print(res)


if __name__ == '__main__':
    main()
