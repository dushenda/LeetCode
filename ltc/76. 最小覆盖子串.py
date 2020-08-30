#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 76. 最小覆盖子串.py
@author     : CALIBRATION
@time       : 2020/5/30 19:41
@description: None
"""
import collections


class Solution(object):
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt = len(t)
        i = 0
        res = (0, float('inf'))
        for j, c in enumerate(s):
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:  # 步骤一：滑动窗口包含了所有T元素
                while True:  # 步骤二：增加i，排除多余元素
                    c = s[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if j - i < res[1] - res[0]:  # 记录结果
                    res = (i, j)
                need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt += 1
                i += 1
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]  # 如果res始终没被更新过，代表无满足条件的结果


def main():
    s = Solution()
    S = "ADOBECODEBANC"
    T = "ABC"
    res = s.minWindow(S, T)
    print(res)


if __name__ == '__main__':
    main()
