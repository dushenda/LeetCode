#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 657. 机器人能否返回原点.py
@author     : CALIBRATION
@time       : 2020/8/28 13:45
@description: None
"""


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        from collections import Counter
        res = Counter(moves)
        return res['U'] == res['D'] and res['L'] == res['R']


def main():
    s = Solution()
    moves = "UD"
    res = s.judgeCircle(moves)
    print(res)


if __name__ == '__main__':
    main()
