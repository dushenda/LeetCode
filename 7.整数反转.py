#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 7.整数反转.py
@author     : CALIBRATION
@time       : 2020/6/2 14:24
@description: None
"""


class Solution(object):
    def reverse(self, x):
        xx = abs(x)
        # li = map(int, str(xx)) or
        li = str(xx)
        li = [int(a) for a in li]
        res = 0
        for i, a in enumerate(li):
            res = res + a * 10 ** i
        if x < 0:
            res = -res
        if res < -2 ** 31 or res > 2 ** 31 - 1:
            return 0
        return res


def main():
    s = Solution()
    res = s.reverse(123)
    print(res)


if __name__ == '__main__':
    main()
