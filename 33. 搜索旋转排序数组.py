#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 33. 搜索旋转排序数组.py
@author     : CALIBRATION
@time       : 2020/7/5 21:45
@description: None
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def bin_search(num, tar):
            l, r = 0, len(num) - 1
            m = (l + r) // 2
            while l < r:
                if tar > num[m]:
                    l = m + 1
                else:
                    r = m
                m = (l + r) // 2
            res = m if num[m] == tar else -1
            return res

        if not nums:
            return -1
        # 第一次二分找数组交接点
        min1, max2 = nums[0], nums[-1]
        l, r = 0, len(nums) - 1
        m = (l + r) // 2  # 左偏
        while nums[m - 1] < nums[m]:
            if nums[m] > max2:
                l = m + 1
            else:
                r = m
            m = (l + r) // 2
        m = len(nums) if m == 0 else m
        num1, num2 = nums[:m], nums[m:]
        if len(num2) > 0:
            res2 = bin_search(num2, target)
            if res2 != -1:
                return res2 + m
        res1 = bin_search(num1, target)
        return res1


def main():
    sol = Solution()
    nums = [1,3,5]
    target = 0
    res = sol.search(nums, target)
    print(res)


if __name__ == '__main__':
    main()
