#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 9.回文数.py
@author     : CALIBRATION
@time       : 2020/6/2 15:28
@description: None
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        li = str(x)
        lens = len(li)
        for i in range(lens // 2):
            if li[i] != li[lens - 1 - i]:
                return False
        return True

    def isPalindrome2(self, x: int) -> bool:
        if x < 0: return False
        div = 1
        while x // div >= 10: div = div * 10
        while x > 0:
            left = x // div
            right = x % 10
            if left != right: return False
            x = (x % div) // 10
            div = div / 100
        return True


def main():
    s = Solution()
    res = s.isPalindrome2(10111)
    print(res)


if __name__ == '__main__':
    main()
