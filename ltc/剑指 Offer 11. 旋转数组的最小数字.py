#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 剑指 Offer 11. 旋转数组的最小数字.py
@author     : CALIBRATION
@time       : 2020/7/22 9:14
@description: None
"""
from typing import List


# class Solution:
#     # 不能使用中点与左边界进行比较！！
#     def minArray(self, numbers: List[int]) -> int:
#         l, r = 0, len(numbers) - 1
#         while l < r:
#             mid = (l + r) // 2
#             if numbers[mid] < numbers[l]:
#                 r = mid
#             if numbers[mid] > numbers[l]:
#                 l = mid + 1
#             else:
#                 l += 1
#         return l


class Solution:
    def minArray(self, numbers: [int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]:
                i = m + 1
            elif numbers[m] < numbers[j]:
                j = m
            else:
                j -= 1
        return numbers[i]


def main():
    numbers = [10, 1, 10, 10, 10]
    sol = Solution()
    res = sol.minArray(numbers)
    print(res)


if __name__ == '__main__':
    main()
