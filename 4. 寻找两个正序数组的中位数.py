#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 4. 寻找两个正序数组的中位数.py
@author     : CALIBRATION
@time       : 2020/6/5 9:35
@description: None
"""
import heapq


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        new_list = sorted(nums1)
        half = len(new_list) // 2
        return (new_list[half] + new_list[~half]) / 2

    def findMedianSortedArrays2(self, nums1, nums2):
        # 部分归并排序+寻找中位数
        new_list = []
        while nums1 != [] or nums2 != []:
            if not nums1:
                new_list.extend(nums2)
                break
            elif not nums2:
                new_list.extend(nums1)
                break
            else:
                if nums1[0] < nums2[0]:
                    new_list.append(nums1.pop(0))
                else:
                    new_list.append(nums2.pop(0))
        # 寻找中位数
        half = len(new_list) // 2
        return (new_list[half] + new_list[~half]) / 2

    def findMedianSortedArrays3(self, nums1, nums2):
        pass


def main():
    s = Solution()
    nums1 = [1, 2]
    nums2 = [-1, 3]
    res = s.findMedianSortedArrays3(nums1, nums2)
    print(res)


if __name__ == '__main__':
    main()
