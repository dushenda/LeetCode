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
        def dfs(candidates, begin, size, path, res, target):
            if target == 0 and path not in res:
                res.append(path[:])
                return
            for index in range(begin, size):
                resi = target - candidates[index]
                if resi < 0: break
                path.append(candidates[index])
                dfs(candidates, index + 1, size, path, res, resi)
                path.pop()

        size = len(candidates)
        if size == 0: return []
        candidates.sort()
        res = []
        path = []
        dfs(candidates, 0, size, path, res, target)
        return res


def main():
    # pass
    import copy
    b = [1, 2, 3, [3, 4, 5]]
    a = b
    c = copy.copy(b)
    d = copy.deepcopy(a)
    print("ida=", id(a[3]), "idb=", id(b[3]), "idc=", id(c[3]), "idd=", id(d[3]))


if __name__ == '__main__':
    main()
