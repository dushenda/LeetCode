#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 41. 缺失的第一个正数.py
@author     : CALIBRATION
@time       : 2020/7/13 10:55
@description: None
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        i = 0
        while i < size:
            if 0 < nums[i] < size and nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                continue
            i += 1
        for i, iv in enumerate(nums):
            if iv != i + 1:
                return i + 1
        return size + 1


def main():
    a = [1, 1]
    sol = Solution()
    res = sol.firstMissingPositive(a)
    print(res)


if __name__ == '__main__':
    main()
