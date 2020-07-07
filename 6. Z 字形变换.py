#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 6. Z 字形变换.py
@author     : CALIBRATION
@time       : 2020/6/17 9:22
@description: None
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        i, flag = 0, -1
        res = ["" for _ in range(numRows)]
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag *= -1
            i = i + flag
        return "".join(res)

def main():
    test = 'LEETCODEISHIRING'
    n = 4
    s = Solution()
    res = s.convert(test, n)
    print(res)


if __name__ == '__main__':
    main()
