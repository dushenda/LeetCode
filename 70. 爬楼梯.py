#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 70. 爬楼梯.py
@author     : CALIBRATION
@time       : 2020/6/13 13:58
@description: None
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        a1, a2 = 1, 2
        if n < 3:
            return n
        for i in range(2, n):
            a1, a2 = a2, a1 + a2
        return a2

    def climbStairs2(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


def main():
    s = Solution()
    res, res2 = s.climbStairs(15), s.climbStairs2(15)
    print(res, '\n', res2)


if __name__ == '__main__':
    main()
