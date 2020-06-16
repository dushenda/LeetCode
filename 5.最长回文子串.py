#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 5.最长回文子串.py
@author     : CALIBRATION
@time       : 2020/6/13 15:09
@description: None
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 暴力法
        if s == s[::-1]:
            return s
        max_len = 1
        res = s[0]
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > max_len:
                    max_len = len(s[i:j])
                    res = s[i:j]
        return res
    def longestPalindrome2(self, s: str) -> str:
        # 中心扩散法
        pass

def main():
    s = Solution()
    res = s.longestPalindrome("abb")
    print(res)


if __name__ == '__main__':
    main()
