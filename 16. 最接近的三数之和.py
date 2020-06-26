#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 16. 最接近的三数之和.py
@author     : CALIBRATION
@time       : 2020/6/23 14:53
@description: None
"""


class Solution:
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        last_resu = float('inf')
        res = float('inf')
        for iv in nums:
            target2 = target - iv
            nums2 = nums
            nums2.remove(iv)
            l, r = 0, len(nums2) - 1
            while l < r:
                resu = nums2[l] + nums2[r] - target2
                if resu > 0:
                    # r左移
                    if last_resu > abs(resu):
                        last_resu = abs(resu)
                        res = iv + nums2[l] + nums2[r]
                    r -= 1
                elif resu < 0:
                    if last_resu > abs(resu):
                        last_resu = abs(resu)
                        res = iv + nums2[l] + nums2[r]
                    l += 1
                else:
                    return target
        return res


def main():
    s = Solution()
    nums = [-1, 2, 1, -4]
    target = 1
    res = s.threeSumClosest(nums, target)
    print(res)


if __name__ == '__main__':
    main()
