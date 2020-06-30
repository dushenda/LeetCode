#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 17. 电话号码的字母组合.py
@author     : CALIBRATION
@time       : 2020/6/23 15:59
@description: None
"""


class Solution:
    def letterCombinations(self, digits: str):
        # Python列表推导式
        KEY = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        if digits == '':
            return []
        ans = ['']
        for num in digits:
            ans = [pre + suf for pre in ans for suf in KEY[num]]
        return ans


def main():
    inp = "23567"
    s = Solution()
    res = s.letterCombinations(inp)
    print(res)


if __name__ == '__main__':
    main()