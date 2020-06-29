#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 28. 实现 strStr().py
@author     : CALIBRATION
@time       : 2020/6/29 19:43
@description: None
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        size1 = len(haystack)
        size2 = len(needle)
        for i in range(size1):
            if haystack[i] == needle[0]:
                for j in range(0, size2):
                    if i + j > size1 - 1:
                        return -1
                    if haystack[i + j] != needle[j]:
                        break
                    if j == size2 - 1:
                        return i
        return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        try:
            res = haystack.index(needle)
        except ValueError:
            res = -1
        return res


def main():
    s = Solution()
    haystack = "aa"
    needle = "aaaa"
    res = s.strStr2(haystack, needle)
    print(res)


if __name__ == '__main__':
    main()
