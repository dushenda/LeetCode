#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 1365. 有多少小于当前数字的数字.py
@author     : CALIBRATION
@time       : 2020/10/26 8:59
@description: None
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            tmp = 0
            for j in range(len(nums)):
                if i != j and nums[i] > nums[j]:
                    tmp += 1
            res.append(tmp)
        return res

    def smallerNumbersThanCurrent2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = [0] * 101

        for n in nums:
            dic[n] += 1

        return [sum(dic[0:n]) for n in nums]

def main():
    nums = [8, 1, 2, 2, 3]
    s = Solution()
    res = s.smallerNumbersThanCurrent2(nums)
    print(res)


if __name__ == '__main__':
    main()
