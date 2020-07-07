#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 378. 有序矩阵中第K小的元素.py
@author     : CALIBRATION
@time       : 2020/7/2 11:37
@description: None
"""


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1  # 因为这个所以可以得到左边的数
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left


def main():
    pass


if __name__ == '__main__':
    main()
