#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 43. 字符串相乘.py
@author     : CALIBRATION
@time       : 2020/7/15 9:01
@description: None
"""


class Solution:
    def multiply(self, num1: str, num2: str):
        m, n = len(num1), len(num2)
        num1, num2 = num1[::-1], num2[::-1]
        res = [0 for _ in range(m + n)]
        for i in range(m):
            for j in range(n):
                res[i + j] += int(num1[i]) * int(num2[j])
        for i in range(1, len(res)):
            res[i] += res[i - 1] // 10
            res[i - 1] = res[i - 1] % 10
        res = res[::-1]
        for i in range(len(res)):
            if res[i] != 0 or i == len(res) - 1:
                res = res[i:]
                break
        res = "".join(map(str, res))
        return res


def main():
    sol = Solution()
    num1 = "2"
    num2 = "3"
    num3 = "9133"
    num4 = "0"
    res = sol.multiply(num3, num4)
    print(res)


if __name__ == '__main__':
    main()
