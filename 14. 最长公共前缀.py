#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 14. 最长公共前缀.py
@author     : CALIBRATION
@time       : 2020/6/15 10:06
@description: None
"""


class Solution:
    def longestCommonPrefix(self, strs):
        res = []
        if not strs:
            return ""
        lens = [len(strx) for strx in strs]
        min_len = min(lens)
        for i in range(min_len):
            s = set([strx[i] for strx in strs])
            if len(s) == 1:
                res.append(strs[0][i])
            else:
                break
        return ''.join(res)

    def longestCommonPrefix2(self, strs):
        ans = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                ans += i[0]
            else:
                break
        return ans


def main():
    s = Solution()
    res = s.longestCommonPrefix(["dog", "racecar", "car"])
    print(res)


if __name__ == '__main__':
    main()
