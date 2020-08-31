#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 剑指 Offer 53 - II. 0～n-1中缺失的数字.py
@author     : CALIBRATION
@time       : 2020/8/31 15:00
@description: None
"""
from typing import List
# 排序数组的搜索问题，首先考虑二分法！

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m: i = m + 1
            else: j = m - 1
        return i


def main():
    pass


if __name__ == '__main__':
    main()
