#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 1051. 高度检查器.py
@author     : CALIBRATION
@time       : 2020/6/13 14:46
@description: None
"""


class Solution:
    def heightChecker(self, heights):
        res = sorted(heights)
        if heights == res:
            return 0
        cnt = 0
        for i in range(len(heights)):
            if res[i] != heights[i]:
                cnt = cnt + 1
        return cnt


def main():
    pass


if __name__ == '__main__':
    a = [1, 2, 3, 0]
    print()
    # main()
