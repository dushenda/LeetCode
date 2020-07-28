#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 38. 外观数列.py
@author     : CALIBRATION
@time       : 2020/6/29 22:44
@description: None
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        if (n == 1): return '1'
        num = self.countAndSay(n - 1) + "*"
        print(num)
        temp = list(num)
        count = 1
        strBulider = ''
        for i in range(len(temp) - 1):
            if temp[i] == temp[i + 1]:
                count += 1
            else:
                strBulider += str(count) + temp[i]
                count = 1
        return strBulider


def main():
    n = 20
    sol = Solution()
    res = sol.countAndSay(n)
    print(res)


if __name__ == '__main__':
    main()
