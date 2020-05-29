#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 18.四数之和.py
@author     : CALIBRATION
@time       : 2020/5/23 16:05
@description: None
"""


class Solution(object):
    def fourSum(self, nums, target):
        # 848ms,13.6MB
        length = len(nums)
        res = []
        nums = sorted(nums)
        for i1 in range(length):
            # 遍历一次全序列，保证四个数从小到大排列
            if i1 > 0 and nums[i1] == nums[i1 - 1]:
                continue
            if i1 > length - 4 or sum(nums[i1:i1 + 4]) > target:
                break
            # 三数之和,nums2→target2
            target2 = target - nums[i1]
            nums2 = nums[i1 + 1:]
            length2 = len(nums2)
            for i2 in range(length2):
                # 遍历剩下的列表，l为左指针，r为右指针
                if i2 > 0 and nums2[i2] == nums2[i2 - 1]:
                    continue
                l = i2 + 1
                r = length2 - 1
                target3 = target2 - nums2[i2]
                while l < r:
                    if l > i2 + 1 and nums2[l] == nums2[l - 1]:
                        l = l + 1
                        continue
                    if r < length2 - 1 and nums2[r] == nums2[r + 1]:
                        r = r - 1
                        continue
                    sumlr = nums2[l] + nums2[r]
                    if sumlr < target3:
                        l = l + 1
                    elif sumlr == target3:
                        res.append([nums[i1], nums2[i2], nums2[l], nums2[r]])
                        l, r = l + 1, r - 1
                    else:
                        r = r - 1
        return res

    def fourSum2(self, nums, target):
        nums = sorted(nums)
        res = []
        # 遍历序列nums，保证从小到大选择数字
        # target3代表三数之和，target2代表两数之和
        for i1, n1 in enumerate(nums):
            if i1 > 0 and n1 == nums[i1 - 1]:
                continue
            target3 = target - n1
            nums3 = nums[i1 + 1:]
            # 三数之和在nums3
            for i2, n2 in enumerate(nums3[:-2]):
                # 双指针法计算三数之和
                if i2 > 0 and n2 == nums3[i2 - 1]:
                    continue
                l = i2 + 1
                r = len(nums3) - 1
                # 剪枝，一开始就删去不合格的部分
                if n2 + nums3[r - 1] + nums3[r] < target3 or n2 + nums3[l] + nums3[l + 1] > target3:
                    continue
                target2 = target3 - n2
                while l < r:
                    if nums3[l] == nums3[l - 1] and l > i2 + 1:
                        l = l + 1
                        continue
                    if r + 1 < len(nums3) and nums3[r] == nums3[r + 1]:
                        r = r - 1
                        continue
                    if nums3[l] + nums3[r] == target2:
                        res.append([n1, n2, nums3[l], nums3[r]])
                        l, r = l + 1, r - 1
                    elif nums3[l] + nums3[r] < target2:
                        l = l + 1
                    else:
                        r = r - 1
        return res


def main():
    s = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    nums2 = [-1, 0, -5, -2, -2, -4, 0, 1, -2]
    target = 0
    target2 = -9
    nums3 = [0, 0, 0, 0]
    target3 = 0
    nums4 = [-1, -5, -5, -3, 2, 5, 0, 4]
    target4 = -7
    res = s.fourSum2(nums, target)
    print(res)


if __name__ == '__main__':
    main()
