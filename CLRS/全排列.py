#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 全排列.py
@author     : CALIBRATION
@time       : 2020/8/11 16:01
@description: None
"""
from typing import List


def permute(s: str) -> List[str]:
    res = []

    def backtrace(nums, path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for iv in nums:
            if iv not in path:
                path.append(iv)
                backtrace(nums, path)
                path.pop()

    backtrace(s, [])
    return res


def main():
    s = "abc"
    res = permute(s)
    print(res)


if __name__ == '__main__':
    main()
