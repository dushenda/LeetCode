#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 归并排序.py
@author     : CALIBRATION
@time       : 2020/6/5 12:13
@description: None
"""
import random
import unittest


class Solution:
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        else:
            # 分开
            mid = len(nums) // 2
            left_half = self.merge_sort(nums[:mid])
            right_half = self.merge_sort(nums[mid:])
            # 合并
            new_list = []
            while left_half != [] or right_half != []:
                if not left_half:
                    new_list.extend(right_half)
                    break
                elif not right_half:
                    new_list.extend(left_half)
                    break
                else:
                    if left_half[0] < right_half[0]:
                        new_list.append(left_half.pop(0))
                    else:
                        new_list.append(right_half.pop(0))
            return new_list


class Test(unittest.TestCase):
    s = Solution()

    def test(self):
        for i in range(10):
            test_data = [random.randint(0, 255) for j in range(20)]
            test_res = sorted(test_data)
            cal_res = self.s.merge_sort(test_data)
            self.assertEqual(test_res, cal_res)


def main():
    t = Test()
    t.test()


if __name__ == '__main__':
    main()
