#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 面试题 16.11. 跳水板.py
@author     : CALIBRATION
@time       : 2020/7/8 10:20
@description: None
"""


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int):
        if k == 0:
            return []
        res = set()
        for i in range(0, k + 1):
            value = shorter * i + longer * (k - i)
            res.add(value)
        return sorted(list(res))


def main():
    sol = Solution()
    shorter = 2
    longer = 1118596
    k = 979
    res = sol.divingBoard(shorter, longer, k)
    print(res)


if __name__ == '__main__':
    main()

