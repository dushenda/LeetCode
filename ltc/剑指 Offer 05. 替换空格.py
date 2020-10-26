#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 剑指 Offer 05. 替换空格.py
@author     : CALIBRATION
@time       : 2020/10/26 10:23
@description: None
"""


class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')


def main():
    s = "We are happy."
    ss = Solution()
    res = ss.replaceSpace(s)
    print(res)


if __name__ == '__main__':
    main()
