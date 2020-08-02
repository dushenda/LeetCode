#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 面试题 08.03. 魔术索引.py
@author     : CALIBRATION
@time       : 2020/7/31 19:39
@description: None
"""
from typing import List


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i, iv in enumerate(nums):
            if i == iv:
                return i
        return -1

def main():
    pass


if __name__ == '__main__':
    main()
