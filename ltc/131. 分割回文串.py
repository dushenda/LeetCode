#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 131. 分割回文串.py
@author     : CALIBRATION
@time       : 2020/9/11 12:14
@description: None
"""
# 需要复习
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrace(s, tmp):
            if len(s) == 0:
                res.append(tmp[:])
                return
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1] and s[:i] != '':
                    tmp.append(s[:i])
                    backtrace(s[i:], tmp)
                    tmp.pop()

        res = []
        backtrace(s, [])
        return res


def main():
    pass


if __name__ == '__main__':
    main()
