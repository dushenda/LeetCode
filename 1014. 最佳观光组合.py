#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 1014. 最佳观光组合.py
@author     : CALIBRATION
@time       : 2020/6/17 8:09
@description: None
"""


class Solution:
    def maxScoreSightseeingPair(self, A) -> int:
        # 暴力法，超出时间限制
        max_score = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i] + A[j] - (j - i) > max_score:
                    max_score = A[i] + A[j] - (j - i)
        return max_score

    def maxScoreSightseeingPair2(self, A) -> int:
        # O(n^2)这个不🆗
        dp = [[0 for _ in A] for _ in A]
        max_score = 0
        for i in range(0, len(A)):
            for j in range(i + 1, len(A)):
                if j - i == 1:
                    dp[i][j] = A[j] + A[i] - 1
                else:
                    dp[i][j] = dp[i][j - 1] - A[j - 1] + A[j] - 1
                if dp[i][j] > max_score:
                    max_score = dp[i][j]
        return max_score

    def maxScoreSightseeingPair3(self, A):
        max_score = 0
        pre_max = A[0] - 0
        for j in range(1, len(A)):
            v = A[j] - j
            pre_max = max(pre_max, A[j - 1] + (j - 1))
            if v + pre_max > max_score:
                max_score = v + pre_max
        return max_score


def main():
    A = [1, 3, 5]
    s = Solution()
    res = s.maxScoreSightseeingPair3(A)
    print(res)


if __name__ == '__main__':
    main()
