#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 剑指 Offer 56 - I. 数组中数字出现的次数.py
@author     : CALIBRATION
@time       : 2020/8/31 15:54
@description: None
"""
from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        k, mask = 0, 1
        for num in nums: k ^= num
        while k & mask == 0: mask <<= 1
        a, b = 0, 0
        for num in nums:
            if num & mask == 0:
                a ^= num
            else:
                b ^= num
        return [a, b]


def main():
    nums = [4, 1, 4, 6]
    s = Solution()
    res = s.singleNumbers(nums)
    print(res)


if __name__ == '__main__':
    main()