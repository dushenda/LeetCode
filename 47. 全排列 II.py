#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 47. 全排列 II.py
@author     : CALIBRATION
@time       : 2020/7/20 14:30
@description: None
"""


class Solution:

    def __init__(self):
        self.res = []

    def permuteUnique(self, nums: list) -> list:
        track = []
        self.backtrace(nums, track)
        for i, iv in enumerate(self.res):
            self.res[i] = ''.join(iv)
        return self.res

    def backtrace(self, nums, track):
        if len(nums) < 1:
            if track not in self.res:
                self.res.append(track.copy())
            return
        for i in range(len(nums)):
            track.append(nums.pop(i))
            self.backtrace(nums, track)
            nums.insert(i, track.pop())


def main():
    nums = "acc"
    sol = Solution()
    res = sol.permuteUnique(list(nums))
    print(res)


if __name__ == '__main__':
    main()
