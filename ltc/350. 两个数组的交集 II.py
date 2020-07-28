#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 350. 两个数组的交集 II.py
@author     : CALIBRATION
@time       : 2020/7/13 8:50
@description: None
"""
from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1, n2 = Counter(nums1), Counter(nums2)
        res = []
        for keys in n2:
            if keys in n1:
                res.extend([keys] * min(n1[keys], n2[keys]))
        return sorted(res)


def main():
    nums1, nums2 = [1, 2, 2, 1], [2, 2]
    nums3, nums4 = [4, 9, 5], [9, 4, 9, 8, 4]
    sol = Solution()
    res = sol.intersect(nums3, nums4)
    print(res)


if __name__ == '__main__':
    main()
