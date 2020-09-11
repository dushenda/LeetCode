#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : perm.py
@author     : CALIBRATION
@time       : 2020/9/9 8:30
@description: None
"""


class Solution:
    res = []

    def backtrace(self, path, nums):
        if len(path) == len(nums):
            self.res.append(path.copy())
            return
        for iv in nums:
            if iv in path: continue
            path.append(iv)
            self.backtrace(path, nums)
            path.pop()


def main():
    s = Solution()
    nums = [1, 2, 3]
    s.backtrace([], nums)
    for iv in s.res:
        print(iv)


if __name__ == '__main__':
    main()
