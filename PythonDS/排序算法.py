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
from typing import List


class Solution:
    def bubleSort(self, nums):
        # 不断前后交换
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                j = i
                while j != 0 and nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    j -= 1
        return nums

    def selectSorted(self, nums):
        n = len(nums)
        for i in range(0, n):
            min_value, idx = nums[i], i
            for j in range(i + 1, n):
                if nums[j] < min_value:
                    min_value, idx = nums[j], j
            nums[i], nums[idx] = nums[idx], nums[i]
        return nums

    def insertSorted(self, nums: List[int]):
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                for j in range(0, i + 1):
                    if nums[i] < nums[j]:
                        nums.insert(j, nums.pop(i))
                        break
        return nums

    def shellSorted(self, nums: List[int]):
        n = len(nums)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = nums[i]
                j = i
                while j - gap >= 0 and nums[j - gap] > temp:
                    nums[j] = nums[j - gap]
                    j -= gap
                nums[j] = temp
            gap = gap // 2
        return nums


def main():
    t = unittest.TestCase()
    s = Solution()
    for i in range(100):
        test_array = [random.randint(0, 1000) for i in range(100)]
        result_array = sorted(test_array)
        t.assertEqual(result_array, s.shellSorted(test_array))


if __name__ == '__main__':
    main()
