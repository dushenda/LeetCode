#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 357. 计算各个位数不同的数字个数.py
@author     : CALIBRATION
@time       : 2020/9/11 11:02
@description: None
"""
# 等使用优化算法

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        nums = range(0, 10)
        cnt = [0]

        def backtrace(nl, track):
            if len(track) == n: return
            for i in nl:
                if track and track[0] == 0: break
                if i in track:
                    if len(track) < n - 1:
                        for i in range(1, n - len(track) + 1):
                            cnt[0] += 10 ** (n - len(track) - i)
                        continue
                    else:
                        cnt[0] += 1
                track.append(i)
                backtrace(nl, track)
                track.pop()

        backtrace(nums, [])
        return 10 ** n - cnt[0]


def main():
    a = 4
    s = Solution()
    res = s.countNumbersWithUniqueDigits(a)
    print(res)


if __name__ == '__main__':
    main()
