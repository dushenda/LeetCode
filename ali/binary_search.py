#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : binary_search.py
@author     : CALIBRATION
@time       : 2020/8/6 8:57
@description: None
"""


def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        m = (r - l) // 2 + l
        if target <= nums[m]:
            r = m
        else:
            l = m + 1
    return nums[l]


def main():
    numns = [1, 2, 3, 4, 5, 6, 7, 8]
    t = 9
    res = binary_search(numns, t)
    print(res)


if __name__ == '__main__':
    main()
