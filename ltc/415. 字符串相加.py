#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 415. 字符串相加.py
@author     : CALIBRATION
@time       : 2020/8/13 16:35
@description: None
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = 0
        num1, num2 = num1[::-1], num2[::-1]
        i = 0
        m, n = len(num1), len(num2)
        while i < min(m, n):
            res += (int(num1[i]) + int(num2[i])) * 10 ** i
            i += 1
        if m > n:
            while i < m:
                res += int(num1[i]) * 10 ** i
                i += 1
        if m < n:
            while i < n:
                res += int(num2[i]) * 10 ** i
                i += 1
        return str(res)

    def addString2(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i > 0 or j > 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res


def main():
    a = "12345"
    b = "1234"
    s = Solution()
    res = s.addStrings(a, b)
    print(res)


if __name__ == '__main__':
    main()
