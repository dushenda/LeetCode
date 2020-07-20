#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 面试题 08.06. 汉诺塔问题.py
@author     : CALIBRATION
@time       : 2020/7/16 20:23
@description: None
"""


class Solution:
    def hanota(self, A: list, B: list, C: list) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        n = len(A)
        self.move(n, A, B, C)
        # 定义move 函数移动汉诺塔

    def move(self, n, A, B, C):
        if n == 1:
            C.append(A.pop())
            return
        self.move(n - 1, A, C, B)  # 将A上面n-1个通过C移到B
        C.append(A.pop())  # 将A最后一个移到C
        self.move(n - 1, B, A, C)  # 将B上面n-1个通过空的A移到C


def main():
    pass


if __name__ == '__main__':
    main()
