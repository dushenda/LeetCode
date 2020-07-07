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


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 暴力法
        if not s:
            return s
        res = s[0]
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                tmp = s[i:j + 1]
                if tmp == tmp[::-1] and len(s[i:j + 1]) > len(res):
                    res = s[i:j + 1]
        return res

    def longestPalindrome2(self, s: str) -> str:
        # 中心扩散法
        begin, lens = 0, 1
        for i in range(len(s)):
            l, r = i, i
            while l > 0 and r < len(s) - 1 and s[l - 1] == s[r + 1]:
                l, r = l - 1, r + 1
            if r - l >= lens:
                begin, lens = l, r - l + 1
            if i < len(s) - 1:
                l, r = i, i + 1
                if s[l] != s[r]:
                    continue
                while l > 0 and r < len(s) - 1 and s[l - 1] == s[r + 1]:
                    l, r = l - 1, r + 1
                if r - l >= lens:
                    begin, lens = l, r - l + 1
        return s[begin:begin + lens]

    def longestPalindrome3(self, s: str) -> str:
        # 动态规划
        table_length = len(s)
        if table_length < 2:
            return s
        dp = [[False for _ in range(table_length)] for _ in range(table_length)]
        begin, lens = 0, 1
        for i in range(0, table_length):
            for j in range(i, -1, -1):
                if s[i] == s[j] and i - j < 3:
                    dp[i][j] = True
                    if i - j >= lens:
                        begin, lens = j, i - j + 1
                elif s[i] == s[j] and dp[i - 1][j + 1]:
                    dp[i][j] = True
                    if i - j >= lens:
                        begin, lens = j, i - j + 1
        return s[begin:begin + lens]


def main():
    s = Solution()
    res = s.longestPalindrome2("cbbd")
    print(res)


if __name__ == '__main__':
    main()
