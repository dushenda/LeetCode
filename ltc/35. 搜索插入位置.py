#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 35. 搜索插入位置.py
@author     : CALIBRATION
@time       : 2020/6/29 22:38
@description: None
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)


def main():
    pass


if __name__ == '__main__':
    main()
