#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 40. 组合总和 II.py
@author     : CALIBRATION
@time       : 2020/7/13 10:19
@description: None
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        res = []
        path = []
        self.__dfs(candidates, 0, size, path, res, target)
        return res

    def __dfs(self, candidates, begin, size, path, res, target):
        if target == 0 and path not in res:
            res.append(path[:])
        for index in range(begin, size):
            residue = target - candidates[index]
            if residue < 0:
                break
            path.append(candidates[index])
            self.__dfs(candidates, index + 1, size, path, res, residue)
            path.pop()


def main():
    pass


if __name__ == '__main__':
    main()
