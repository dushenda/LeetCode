#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 细胞分裂-递归.py
@author     : CALIBRATION
@time       : 2020/7/16 21:43
@description: None
"""
import unittest


class Solution:
    def all_cells(self, n):
        return self.a_cell(n) + self.b_cell(n) + self.c_cell(n)

    def a_cell(self, n):
        if n == 1:
            return 1
        return self.a_cell(n - 1) + self.b_cell(n - 1) + self.c_cell(n - 1)

    def b_cell(self, n):
        if n == 1:
            return 0
        return self.a_cell(n - 1)

    def c_cell(self, n):
        if n == 1 or n == 2:
            return 0
        return self.b_cell(n - 1)

    def cells(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        elif n == 4:
            return 7
        return 2 * self.cells(n - 1) - self.cells(n - 4)


def main():
    test = unittest.TestCase()
    for n in range(1, 20):
        sol = Solution()
        res1 = sol.all_cells(n)
        res2 = sol.cells(n)
        test.assertEqual(res1, res2)


if __name__ == '__main__':
    main()
