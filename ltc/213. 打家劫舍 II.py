#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 213. 打家劫舍 II.py
@author     : CALIBRATION
@time       : 2020/8/5 17:05
@description: None
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # 2次动态规划，1次包含房子1，1次不包含房子1
        lens = len(nums) + 1
        dp1 = [0 for _ in range(lens)]
        dp2 = [0 for _ in range(lens)]
        dp1[1] = nums[0]
        for i in range(2, lens):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i - 1])
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i - 1])
        return max(dp1[lens - 2], dp2[lens - 1])


def main():
    pass


if __name__ == '__main__':
    main()
