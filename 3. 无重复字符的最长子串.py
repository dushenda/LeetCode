#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 3. 无重复字符的最长子串.py
@author     : CALIBRATION
@time       : 2020/5/30 15:59
@description: None
"""
import collections


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res = 0
        deque = collections.deque()
        for n in s:
            while n in deque:
                deque.popleft()
            deque.append(n)
            lens = len(deque)
            if lens > res:
                res = lens
        return res
    def lengthOfLongestSubstring2(self,s):
        res = 0


def main():
    s = Solution()
    str = "abcabcbb"
    res = s.lengthOfLongestSubstring(str)
    print(res)


if __name__ == '__main__':
    main()