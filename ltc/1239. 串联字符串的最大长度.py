#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 1239. 串联字符串的最大长度.py
@author     : CALIBRATION
@time       : 2020/9/14 10:54
@description: None
"""
from typing import List


# class Solution:
#     def maxLength(self, arr: List[str]) -> int:
#         self.res = 0
#         self.max_len = len(''.join(arr))
#
#         def backtract(arrs, s):
#             if self.res == self.max_len: return
#             # ["ab", "cd", "cde", "cdef", "efg", "fgh", "abxyz"]
#             for i in range(len(arrs)):
#                 tmp = arrs[i]
#                 s = s + tmp
#                 if len(set(s)) == len(s):
#                     self.res = max(self.res, len(s))
#                 else:
#
#                 arrs.pop(i)
#                 backtract(arrs, s)
#                 arrs.insert(i, tmp)
#                 s = s[:-len(tmp)]
#
#         backtract(arr, '')
#         return self.res

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        t = []
        for i in arr:  # 去重
            if len(i) == len(set(i)):
                t.append(i)
        arrs = t[:]

        def dfs(i, cur):
            if i >= len(arrs):
                return len(cur)
            if not (set(cur) & set(arrs[i])):  # 判断集合是否相交
                # 若不相交，则要判断当前arrs[i]是否要取，因为若取，可能导致后面更长的字符串和当前字符串重复而无法取
                return max(dfs(i + 1, cur + arrs[i]), dfs(i + 1, cur))
            else:
                return dfs(i + 1, cur)

        lens = dfs(0, '')
        return lens


def main():
    arr = ["ab", "cd", "cde", "cdef", "efg", "fgh", "abxyz"]
    s = Solution()
    res = s.maxLength(arr)
    print(res)


if __name__ == '__main__':
    main()
