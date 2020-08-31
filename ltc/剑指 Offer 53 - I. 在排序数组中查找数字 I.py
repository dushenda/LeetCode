#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 剑指 Offer 53 - I. 在排序数组中查找数字 I.py
@author     : CALIBRATION
@time       : 2020/8/31 14:46
@description: None
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return 0

        def bs(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = l + (r - l) // 2
                if target <= nums[m]: r = m
                if target > nums[m]: l = m + 1
            return l

        pos = bs(nums, target)
        if nums[pos] != target: return 0
        pos_l, pos_r = pos, pos
        while pos_l > 0 and nums[pos_l] == target: pos_l -= 1
        while pos_r < len(nums) - 1 and nums[pos_r] == target: pos_r += 1
        if nums[pos_l] != target: pos_l += 1
        if nums[pos_r] != target: pos_r -= 1
        return pos_r - pos_l + 1

    def search2(self, nums: List[int], target: int) -> int:
        def helper(tar):
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] <= tar: l = m + 1
                else: r = m - 1
            return l

        return helper(target) - helper(target - 1)


def main():
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    s = Solution()
    res = s.search(nums, target)
    print(res)


if __name__ == '__main__':
    main()
