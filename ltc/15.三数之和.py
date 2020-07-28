#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 15.三数之和.py
@author     : CALIBRATION
@time       : 2020/5/21 22:42
@description: None
"""
import unittest


class Solution(object):
    def threeSum(self, nums):
        """
        超出时间限制
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        r = len(nums)
        res = []
        i1_used = []
        i2_used = []
        i3_used = []
        for i1 in range(r):
            if nums[i1] in i1_used:
                continue
            i1_used.append(nums[i1])
            i2_used.clear()
            for i2 in range(i1 + 1, r):
                if nums[i2] in i2_used:
                    continue
                i2_used.append(nums[i2])
                i3_used.clear()
                for i3 in range(i2 + 1, r):
                    if nums[i3] in i3_used:
                        continue
                    i3_used.append(nums[i3])
                    if nums[i1] + nums[i2] + nums[i3] == 0:
                        res.append([nums[i1], nums[i2], nums[i3]])
        return res

    def threeSum2(self, nums):
        """
        双指针无重复
        :param nums:
        :return:
        """
        res = []
        nums = sorted(nums)
        a = len(nums)
        for i in range(0, a - 2):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                # 因为是已经排序之后的序列
                continue
            l, r = i + 1, a - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l = l + 1
                elif nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r - 1]:
                        r = r - 1
                    l, r = l + 1, r - 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r = r - 1
        return res


class Test(unittest.TestCase):
    s = Solution()
    inputs = [[-1, 0, 1, 2, -1, -4], [0, 0, 0, 0], [-2, 0, 0, 2, 2]]
    res = [[[-1, -1, 2], [-1, 0, 1]], [[0, 0, 0]], [[-2, 0, 2]]]

    def test(self):
        for i in range(3):
            self.assertEqual(self.s.threeSum2(self.inputs[i]), self.res[i])


def main():
    t = Test()
    t.test()


if __name__ == '__main__':
    main()
