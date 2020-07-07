#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 12. 整数转罗马数字.py
@author     : CALIBRATION
@time       : 2020/6/22 20:34
@description: None
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1000, 500, 100, 50, 10, 5, 1]
        sym = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        res = []
        for i in range(len(nums)):
            q, num = num // nums[i], num % nums[i]
            if i > 1 and q == 4:
                if res[-1] == sym[i - 1]:
                    res.pop()
                    res.append(sym[i] + sym[i - 2])
                else:
                    res.append(sym[i] + sym[i - 1])
            else:
                res.append(sym[i] * q)
        return ''.join(res)


def main():
    a = 1994
    s = Solution()
    res = s.intToRoman(a)
    print(res)


if __name__ == '__main__':
    main()
