#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 46. 全排列.py
@author     : CALIBRATION
@time       : 2020/7/20 13:35
@description: None
"""


class Solution:

    def __init__(self):
        self.res = []

    def permute(self, nums: list) -> list:
        track = []
        self.backtrace(nums, track)
        return self.res

    def backtrace(self, nums, track):
        if len(nums) < 1:
            self.res.append(track.copy())
            return
        for i in range(len(nums)):
            track.append(nums.pop(i))
            self.backtrace(nums, track)
            nums.insert(i, track.pop())


def main():
    nums = [1, 2, 3]
    sol = Solution()
    res = sol.permute(nums)
    print(res)


if __name__ == '__main__':
    main()
