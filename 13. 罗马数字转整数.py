#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 13. 罗马数字转整数.py
@author     : CALIBRATION
@time       : 2020/6/22 21:15
@description: None
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        sym2nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        if len(s) == 1:
            return sym2nums[s]
        else:
            res = 0
            for i in range(len(s) - 1):
                if sym2nums[s[i]] < sym2nums[s[i + 1]]:
                    res += sym2nums[s[i + 1]] - sym2nums[s[i]]


def main():
    pass


if __name__ == '__main__':
    main()
