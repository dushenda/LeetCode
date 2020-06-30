#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 454.四数相加.py
@author     : CALIBRATION
@time       : 2020/5/29 13:26
@description: None
"""
import collections


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB = []
        hashAB = {}
        res = 0
        lens = len(A)
        for i1 in range(lens):
            for i2 in range(lens):
                AB.append(A[i1] + B[i2])
        for key in AB:
            hashAB[key] = hashAB.get(key, 0) + 1
        for i3 in range(lens):
            for i4 in range(lens):
                target = 0 - (C[i3] + D[i4])
                res = res + hashAB.get(target, 0)
        return res

    def fourSumCount2(self, A, B, C, D):
        lookup = collections.defaultdict(int)
        res = 0
        for a in A:
            for b in B:
                lookup[a + b] += 1
        for c in C:
            for d in D:
                res += lookup[-(c + d)]
        return res

    def fourSumCount3(self, A, B, C, D):
        AB = []
        res = 0
        for a in A:
            for b in B:
                AB.append(a + b)
        hashAB = collections.Counter(AB)
        for c in C:
            for d in D:
                res = res + hashAB.get(-(c + d), 0)
        return res


def main():
    s = Solution()
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    res = s.fourSumCount3(A, B, C, D)
    print(res)


if __name__ == '__main__':
    main()
