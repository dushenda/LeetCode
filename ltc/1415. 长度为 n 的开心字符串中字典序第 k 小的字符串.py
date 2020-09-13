#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 1415. 长度为 n 的开心字符串中字典序第 k 小的字符串.py
@author     : CALIBRATION
@time       : 2020/9/11 13:41
@description: None
"""


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        chars = ['a', 'b', 'c']
        res = []

        def backtrace(strs, track):
            if len(res) == k: return
            if len(track) == n:
                res.append(track.copy())
                return
            for iv in strs:
                if track and iv == track[-1]: continue
                track.append(iv)
                backtrace(strs, track)
                track.pop()

        backtrace(chars, [])
        return ''.join(res[-1] if k <= len(res) else '')


def main():
    n, k = 1, 4
    s = Solution()
    res = s.getHappyString(n, k)
    print(res)


if __name__ == '__main__':
    main()
