#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 排序算法.py
@author     : CALIBRATION
@time       : 2020/6/23 16:53
@description: None
"""
import unittest
import random


class Solution:
    def bubleSort(self, nums):
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                j = i
                while j != 0 and nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    j -= 1
        return nums


def main():
    t = unittest.TestCase()
    s = Solution()
    for i in range(100):
        test_array = [random.randint(0, 1000) for i in range(100)]
        result_array = sorted(test_array)
        t.assertEqual(result_array, s.bubleSort(test_array))


if __name__ == '__main__':
    main()
