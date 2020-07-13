#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 42. 接雨水.py
@author     : CALIBRATION
@time       : 2020/7/13 13:58
@description: None
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 逐行求解，超时
        if not height:
            return 0
        maxlen = max(height)
        res = 0
        for level in range(1, maxlen + 1):
            temp = 0
            begin = False
            for x in height:
                if x < level:
                    if begin:
                        temp += 1
                else:
                    if not begin:
                        begin = True
                    res += temp
                    temp = 0
        return res

    def trap2(self, height):
        # 按列求解,居然可以通过，不过成绩惨不忍睹
        if not height:
            return 0
        size = len(height)
        res = 0
        for i in range(1, size - 1):
            max_left = max(height[:i])
            max_right = max(height[i + 1:])
            min_height = min(max_left, max_right)
            heightx = min_height - height[i] if min_height > height[i] else 0
            res += heightx
        return res

    def trap3(self, height):
        if not height:
            return 0

        # 动态规划优化求解最值问题
        # 优化左右最高的墙的计算
        def dp_get(heights, lens, dire):
            dp = [0 for i in range(lens)]
            for i in range(1, lens):
                dp[i] = max(dp[i - 1], heights[i - 1])
            if dire == 'left':
                return dp
            if dire == 'right':
                return dp[::-1]

        size = len(height)
        res = 0
        dp_left = dp_get(height, size, 'left')  # 左边的最高
        dp_right = dp_get(height[::-1], size, 'right')  # 右边的最高
        for i in range(1, size):
            min_height = min(dp_left[i], dp_right[i])
            heightx = min_height - height[i] if min_height > height[i] else 0
            res += heightx
        return res

    def trap4(self, hight):
        pass


def main():
    sol = Solution()
    a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    a2 = []
    a3 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    res = sol.trap3(a)
    print(res)


if __name__ == '__main__':
    main()
