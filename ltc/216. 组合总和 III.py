#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 216. 组合总和 III.py
@author     : CALIBRATION
@time       : 2020/9/11 10:30
@description: None
"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = range(1, 10)
        res = []

        def backtrace(nl, target, track):
            if target < 0: return
            if len(track) == k:
                if target == 0: res.append(track.copy())
                return
            for iv in nl:
                if track and iv <= track[-1]: continue
                track.append(iv)
                target -= iv
                backtrace(nl, target, track)
                target += track.pop()

        backtrace(nums, n, [])
        return res


def main():
    k, n = 3, 9
    s = Solution()
    res = s.combinationSum3(k, n)
    print(res)


if __name__ == '__main__':
    main()
