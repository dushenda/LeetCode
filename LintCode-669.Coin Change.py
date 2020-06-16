#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : LintCode-669.Coin Change.py
@author     : CALIBRATION
@time       : 2020/6/13 16:45
@description: None
"""
import math


# Coin:2,5,7
# 27=5*4+7(5个)
# price:input
# output:min coins
class Solution:
    def min_coins(self, n):
        opt = {1: math.inf, 2: 1, 3: math.inf, 4: 2, 5: 1, 6: 3, 7: 1, 8: 4}
        for i in range(9, n + 1):
            residue1 = opt[i - 2]
            residue2 = opt[i - 5]
            residue3 = opt[i - 7]
            opt[i] = min([residue1, residue2, residue3]) + 1
        return opt[n]


def main():
    s = Solution()
    n = 27
    res = s.min_coins(n)
    print(res)


if __name__ == '__main__':
    main()
