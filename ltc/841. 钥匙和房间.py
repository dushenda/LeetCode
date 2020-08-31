#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 841. 钥匙和房间.py
@author     : CALIBRATION
@time       : 2020/8/31 8:51
@description: None
"""
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:# iteration
        if not rooms: return True
        has_unlock = {0}
        stack = rooms[0].copy()
        while stack:
            tmp = stack.pop()
            has_unlock.add(tmp)
            for iv in rooms[tmp]:
                if iv not in has_unlock:
                    stack.append(iv)
        return len(has_unlock) == len(rooms)

    def canVisitAllRooms2(self, rooms: List[List[int]]) -> bool:# recursion
        s = set()
        def dfs(n):
            if n in s: return
            s.add(n)
            for iv in rooms[n]:
                if iv not in s:
                    dfs(iv)
        dfs(0)
        return len(s) == len(rooms)


def main():
    a = [[1, 3], [3, 0, 1], [2], [0]]
    s = Solution()
    res = s.canVisitAllRooms(a)
    print(res)


if __name__ == '__main__':
    main()
