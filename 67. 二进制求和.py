#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 67. 二进制求和.py
@author     : CALIBRATION
@time       : 2020/6/23 10:48
@description: None
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


def main():
    a = "1010"
    b = "1011"
    s = Solution()
    res = s.addBinary(a, b)
    print(res)


if __name__ == '__main__':
    main()
