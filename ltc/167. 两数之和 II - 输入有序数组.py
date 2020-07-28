#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 167. 两数之和 II - 输入有序数组.py
@author     : CALIBRATION
@time       : 2020/7/20 9:17
@description: None
"""


class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        a, b = 0, len(numbers) - 1
        while a < b:
            if numbers[a] + numbers[b] == target:
                return [a, b]
            elif numbers[a] + numbers[b] < target:
                a += 1
            else:
                b -= 1
        return [-1, -1]


def main():
    pass


if __name__ == '__main__':
    main()
