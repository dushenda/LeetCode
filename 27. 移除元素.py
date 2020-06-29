#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 27. 移除元素.py
@author     : CALIBRATION
@time       : 2020/6/29 19:33
@description: None
"""


class Solution:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)


def main():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    s = Solution()
    res = s.removeElement(nums, val)
    print(res)


if __name__ == '__main__':
    main()
