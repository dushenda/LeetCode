#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 844. 比较含退格的字符串.py
@author     : CALIBRATION
@time       : 2020/10/19 8:27
@description: None
"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s, t = [], []
        for i in range(len(S)):
            if S[i] == '#':
                if s: s.pop()
            else: s.append(S[i])
        for i in range(len(T)):
            if T[i] == '#':
                if t: t.pop()
            else: t.append(T[i])
        return s == t


def main():
    s = Solution()
    S, T = "a##c", "#a#c"
    res = s.backspaceCompare(S, T)
    print(res)


if __name__ == '__main__':
    main()
