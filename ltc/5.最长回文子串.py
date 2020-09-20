#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 5.最长回文子串.py
@author     : CALIBRATION
@time       : 2020/6/13 15:09
@description: None
"""


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         # 暴力法
#         if not s:
#             return s
#         res = s[0]
#         for i in range(len(s)):
#             for j in range(i + 1, len(s)):
#                 tmp = s[i:j + 1]
#                 if tmp == tmp[::-1] and len(s[i:j + 1]) > len(res):
#                     res = s[i:j + 1]
#         return res
#
#     def longestPalindrome2(self, s: str) -> str:
#         # 中心扩散法
#         begin, lens = 0, 1
#         for i in range(len(s)):
#             l, r = i, i
#             while l > 0 and r < len(s) - 1 and s[l - 1] == s[r + 1]:
#                 l, r = l - 1, r + 1
#             if r - l >= lens:
#                 begin, lens = l, r - l + 1
#             if i < len(s) - 1:
#                 l, r = i, i + 1
#                 if s[l] != s[r]:
#                     continue
#                 while l > 0 and r < len(s) - 1 and s[l - 1] == s[r + 1]:
#                     l, r = l - 1, r + 1
#                 if r - l >= lens:
#                     begin, lens = l, r - l + 1
#         return s[begin:begin + lens]
#
#     def longestPalindrome3(self, s: str) -> str:
#         # 动态规划
#         table_length = len(s)
#         if table_length < 2:
#             return s
#         dp = [[False for _ in range(table_length)] for _ in range(table_length)]
#         begin, lens = 0, 1
#         for i in range(0, table_length):
#             for j in range(i, -1, -1):
#                 if s[i] == s[j] and i - j < 3:
#                     dp[i][j] = True
#                     if i - j >= lens:
#                         begin, lens = j, i - j + 1
#                 elif s[i] == s[j] and dp[i - 1][j + 1]:
#                     dp[i][j] = True
#                     if i - j >= lens:
#                         begin, lens = j, i - j + 1
#         return s[begin:begin + lens]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1: return s
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 2, n):
                if s[i] == s[j] and dp[i + 1][j - 1] == 1:
                    dp[i][j] = 1
        print(dp)

    def foo2(self, s: str) -> str:
        size = len(s)
        if size < 2: return s
        max_len = 1
        res = s[0]
        for i in range(size):
            odd, odd_len = self.__center_spread(s, size, i, i)
            even, even_len = self.__center_spread(s, size, i, i + 1)
            cur_max_sub = odd if odd_len > even_len else even
            if len(cur_max_sub) > max_len:
                max_len = len(cur_max_sub)
                res = cur_max_sub
        return res

    def __center_spread(self, s, size, left, right):
        i, j = left, right
        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1:j], j - i - 1


def main():
    s = Solution()
    res = s.longestPalindrome("babad")
    print(res)


if __name__ == '__main__':
    main()
