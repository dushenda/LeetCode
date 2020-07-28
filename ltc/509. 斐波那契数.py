#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 509. 斐波那契数.py
@author     : CALIBRATION
@time       : 2020/7/20 10:44
@description: None
"""


class Solution:
    def fib(self, N: int) -> int:
        a, b = 0, 1
        for i in range(1, N):
            a, b = b, a + b
        return b


def main():
    pass


if __name__ == '__main__':
    main()
