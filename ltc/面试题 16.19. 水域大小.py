#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 面试题 16.19. 水域大小.py
@author     : CALIBRATION
@time       : 2020/9/10 14:06
@description: None
"""
from typing import List


# class Solution:
#     def pondSizes(self, land: List[List[int]]) -> List[int]:
#         def dfs(lands, travs, n, m, num):
#             for i in range(n):
#                 for j in range(m):
#                     if travs[i][j]: continue
#                     travs[i][j] = True
#                     if lands[i][j] == 0:
#                         if i > 0 and j > 0:
#                             dfs(lands[i - 1][j - 1], travs, n, m, num + 1)
#                         else:
#                             if i > 0: dfs(lands[i - 1][j], travs, n, m, num + 1)
#                             if j > 0: dfs(lands[i][j - 1], travs, n, m, num + 1)
#
#                             else:
#                                 res.append(num)
#                                 return
#
#         n, m = len(land), len(land[0])
#         traverse = [[False] * m] * n
#         res = []
#         dfs(land, traverse, n, m, 0)
#         return res


class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:

        def dfs(i, j):
            if i < 0 or j < 0 or i > m - 1 or j > n - 1: return
            if land[i][j] != 0: return
            land[i][j] = -1
            res[-1] += 1
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j - 1)
            dfs(i + 1, j + 1)
            dfs(i - 1, j + 1)
            dfs(i + 1, j - 1)

        res = []
        m, n = len(land), len(land[0])
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0:
                    res.append(0)
                    dfs(i, j)
        res.sort()
        return res


def main():
    a = [[0, 2, 1, 0],
         [0, 1, 0, 1],
         [1, 1, 0, 1],
         [0, 1, 0, 1]]
    s = Solution()
    res = s.pondSizes(a)
    print(res)


if __name__ == '__main__':
    main()
