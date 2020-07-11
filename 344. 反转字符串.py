#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 344. 反转字符串.py
@author     : CALIBRATION
@time       : 2020/7/8 11:03
@description: None
"""


class Solution:
    def reverseString(self, s) -> None:
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)


def main():
    sol = Solution()
    sol.reverseString(["h", "e", "l", "l", "o"])


if __name__ == '__main__':
    main()
