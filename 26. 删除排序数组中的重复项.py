#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 26. 删除排序数组中的重复项.py
@author     : CALIBRATION
@time       : 2020/6/29 19:22
@description: None
"""


class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i, res = 0, 1
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
                res += 1
            j += 1
        return res


def main():
    nums = []
    s = Solution()
    res = s.removeDuplicates(nums)
    print(res)


if __name__ == '__main__':
    main()
