#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 30. 串联所有单词的子串.py
@author     : CALIBRATION
@time       : 2020/7/5 15:18
@description: None
"""
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words):
        if not words: return []
        pattern = Counter(words)
        res = []
        wsLen = len(words)
        wLen = len(words[0])
        for i in range(len(s) - wLen * wsLen + 1):
            cur = [s[i + j * wLen:i + (j + 1) * wLen] for j in range(wsLen)]
            if Counter(cur) == pattern: res.append(i)
        return res


def main():
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    sol = Solution()
    res = sol.findSubstring(s, words)
    print(res)


if __name__ == '__main__':
    main()
