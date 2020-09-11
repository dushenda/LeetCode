#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : sort.py
@author     : CALIBRATION
@time       : 2020/9/9 14:36
@description: None
"""


def merge(left, right):
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    if left: res.extend(left)
    if right: res.extend(right)
    return res


def merge_sort(nums):
    if len(nums) < 2: return nums
    mid = len(nums) // 2
    left, right = nums[0:mid], nums[mid:]
    return merge(merge_sort(left), merge_sort(right))


def main():
    nums = [1, 2, 3, 45, 7, 6, 5, 4, 2]
    res = merge_sort(nums)
    print(res)


if __name__ == '__main__':
    main()
