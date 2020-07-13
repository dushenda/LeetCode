#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 剑指 Offer 03. 数组中重复的数字.py
@author     : CALIBRATION
@time       : 2020/7/13 10:48
@description: None
"""
from collections import Counter


class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ll = Counter(nums)
        for x in ll:
            if ll[x] > 1:
                return x
        return -1


def main():
    a = [2, 3, 1, 0, 2, 5, 3]
    sol = Solution()
    res = sol.findRepeatNumber(a)
    print(res)


if __name__ == '__main__':
    main()
