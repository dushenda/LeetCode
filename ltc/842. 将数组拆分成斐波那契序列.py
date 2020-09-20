#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 842. 将数组拆分成斐波那契序列.py
@author     : CALIBRATION
@time       : 2020/9/13 16:13
@description: None
"""
from typing import List


class Solution:

    def splitIntoFibonacci(self, S: str) -> List[int]:
        res = []
        res = self.dfs(S, res, S)
        return res if res else []

    def dfs(self, s, res, A):
        if len(s) == 0: return res
        for i in range(1, len(s) + 1):
            if len(s[:i]) > 1 and s[0] == '0': break
            if len(res) < 2 or res[-1] + res[-2] == int(s[:i]):
                if int(s[:i]) > 2 ** 31: break
                res.append(int(s[:i]))
                self.dfs(s[i:], res, A)
                if len(res) > 2 and ''.join(list(map(str, res))) == A: return res
                res.pop()


def main():
    s = Solution()
    a = "3611537383985343591834441270352104793375145479938855071433500231900737525076071514982402115895535257195564161509167334647108949738176284385285234123461518508746752631120827113919550237703163294909"
    res = s.splitIntoFibonacci(a)
    print(res)


# 输出：[123,456,579]


if __name__ == '__main__':
    main()
