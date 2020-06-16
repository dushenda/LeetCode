#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 面试题 08.11. 硬币.py
@author     : CALIBRATION
@time       : 2020/6/15 9:37
@description: None
"""
import math


class Solution:
    def waysToChange(self, n: int) -> int:
        charges = [1, 5, 10, 25]
        res_list = {0: 0}
        for i in range(1, n + 1):
            res_list[i] = 0
            if i in charges:
                res_list[i] = res_list[i] + 1
            tmp = charges.copy()
            for j in tmp:
                if j < i:
                    res_list[i] = res_list[i] + res_list[j] * res_list[i - j]
                    if i - j in tmp:
                        tmp.remove(i - j)
        return res_list


def main():
    s = Solution()
    res = s.waysToChange(10)
    print(res)


if __name__ == '__main__':
    main()
