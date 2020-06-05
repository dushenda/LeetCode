#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 二分查找.py
@author     : CALIBRATION
@time       : 2020/6/5 18:29
@description: None
"""
import random


class Algorithms:
    def binary_search(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low < high:
            # left point
            mid = (low + high) // 2
            if target <= nums[mid]:
                high = mid
            else:
                low = mid + 1
        return nums[low]

    def binary_search1(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return True
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return False


def main():
    nums = [random.randint(0, 100) for i in range(10)]
    nums = sorted(nums)
    target = 33
    s = Algorithms()
    res = s.binary_search1(nums, target)
    print("nums=", nums, "\n", "target=", target, "\n", "target is in:", res)


if __name__ == '__main__':
    main()
