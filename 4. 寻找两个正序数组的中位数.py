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
import math


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # T = O(m+n)   S = O(m+n)
        nums1.extend(nums2)
        new_list = sorted(nums1)
        half = len(new_list) // 2
        return (new_list[half] + new_list[~half]) / 2

    def findMedianSortedArrays2(self, nums1, nums2):
        # 部分归并排序+寻找中位数
        # T = O(m+n)   S = O(m+n)
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
        # T = O((m+n)/2)
        # 移动m+n/2+1次
        n1 = len(nums1)
        n2 = len(nums2)
        lens = n1 + n2
        left, right = -1, -1
        start1, start2 = 0, 0
        for i in range(lens // 2 + 1):
            left = right
            if start1 < n1 and (start2 >= n2 or nums1[start1] < nums2[start2]):
                right = nums1[start1]
                start1 = start1 + 1
            else:
                right = nums2[start2]
                start2 = start2 + 1
        if lens % 2 == 0:
            return (left + right) / 2
        else:
            return right

    def findMedianSortedArrays4(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            # min(m,n)
            return self.findMedianSortedArrays4(nums2, nums1)
        k = (n1 + n2 + 1) // 2
        left = 0
        right = n1
        while left < right:
            # 二分查找
            m1 = left + (right - left) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2 - 1]:
                left = m1 + 1
            else:
                right = m1
        m1 = left
        m2 = k - m1
        c1 = max(nums1[m1 - 1] if m1 > 0 else float("-inf"), nums2[m2 - 1] if m2 > 0 else float("-inf"))
        if (n1 + n2) % 2 == 1:
            return c1
        c2 = min(nums1[m1] if m1 < n1 else float("inf"), nums2[m2] if m2 < n2 else float("inf"))
        return (c1 + c2) / 2

    def findMedianSortedArrays5(self, nums1, nums2):
        # O(log(min(m,n)))
        x = len(nums1)
        y = len(nums2)

        if x > y:
            return self.findMedianSortedArrays5(nums2, nums1)

        low = 0
        high = x
        while low <= high:
            partition_x = (low + high) // 2
            partition_y = (x + y + 1) // 2 - partition_x

            # if partitionX is 0 it means nothing is there on left side. Use -INF for maxLeftX
            # if partitionX is length of input then there is nothing on right side. Use +INF for minRightX
            if partition_x == 0:
                max_left_x = -math.inf
            else:
                max_left_x = nums1[partition_x - 1]
            if partition_x == x:
                min_right_x = math.inf
            else:
                min_right_x = nums1[partition_x]

            if partition_y == 0:
                max_left_y = -math.inf
            else:
                max_left_y = nums2[partition_y - 1]
            if partition_y == y:
                min_right_y = math.inf
            else:
                min_right_y = nums2[partition_y]

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (x + y) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y:
                # 代表x右边太多了
                high = partition_x - 1
            else:
                low = partition_x + 1


def main():
    s = Solution()
    # nums1 = [-1, 1, 3, 5, 7, 9]
    #
    # nums2 = [2, 4, 6, 8, 10, 12, 14, 16]
    nums1 = [0, 0]
    nums2 = [0, 0]
    res = s.findMedianSortedArrays5(nums1, nums2)
    print(res)


if __name__ == '__main__':
    main()
