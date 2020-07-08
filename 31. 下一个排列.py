#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 31. 下一个排列.py
@author     : CALIBRATION
@time       : 2020/7/5 18:15
@description: None
"""
import bisect

class Solution():
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = len(nums) - 1
        while index > 0:
            if nums[index] > nums[index - 1]:
                break
            index -= 1

        if index > 0:
            nums[index:] = sorted(nums[index:])
            swap_index = bisect.bisect(nums, nums[index - 1], lo=index)
            nums[swap_index], nums[index - 1] = nums[index - 1], nums[swap_index]
        else:
            nums.reverse()


def main():
    nums = [1, 3, 2]
    sol = Solution()
    res = sol.nextPermutation(nums)
    print(res)


if __name__ == '__main__':
    main()
