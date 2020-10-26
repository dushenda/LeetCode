#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 剑指 Offer 04. 二维数组中的查找.py
@author     : CALIBRATION
@time       : 2020/10/26 9:23
@description: None
"""
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix[0])==0: return False
        i, j = 0, len(matrix[0]) - 1
        while matrix[i][j] != target and i < len(matrix) and j >= 0:
            if matrix[i][j] < target:
                if i == len(matrix) - 1: break
                i += 1
            elif matrix[i][j] > target:
                if j == 0: break
                j -= 1
        return matrix[i][j] == target


def main():
    matrix = [[5],[6]]
    target = 6
    s = Solution()
    res = s.findNumberIn2DArray(matrix, target)
    print(res)


if __name__ == '__main__':
    main()
