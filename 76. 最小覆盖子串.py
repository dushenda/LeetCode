#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 76. 最小覆盖子串.py
@author     : CALIBRATION
@time       : 2020/5/30 19:41
@description: None
"""
import collections


class Solution(object):
    def minWindow(self, s, t):
        res = ""
        deque = collections.deque()
        lens = 1e10
        for si in s:
            if len(deque) == 0 and si not in t:
                continue
            deque.append(si)
            while si in t and res != "" and si in deque:
                # 删除si前面的数字（重复）
                deque.popleft()
            while res != "":
                ss = deque.popleft()
                if ss in t:
                    deque.appendleft(ss)
                    break
            if self.isin(t, deque):
                if len(deque) < lens:
                    lens = len(deque)
                    res = "".join(deque)
        return res

    def isin(self, a, b):
        # 判断a是都是b的子集，输入a，b字符串、列表或者队列
        a = list(a)
        b = list(b)
        res = False
        for aa in a:
            res = aa in b
            if res:
                b.remove(aa)
            else:
                break
        return res


def main():
    s = Solution()
    S = "ADOBECODEBANC"
    T = "ABC"
    S2 = "a"
    T2 = "aa"
    S3 = "ab"
    T3 = "b"
    res = s.minWindow(S, T)
    print(res)


if __name__ == '__main__':
    main()