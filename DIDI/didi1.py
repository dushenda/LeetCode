#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : didi1.py
@author     : CALIBRATION
@time       : 2020/8/21 19:02
@description: None
"""


def foo(n):
    res1 = 0
    res2 = []
    for a in range(1, 10):
        for b in range(10):
            for c in range(10):
                if a != b and a != c and b != c:
                    v1 = a * 100 + b * 10 + c
                    v2 = a * 100 + c * 10 + c
                    if v1 + v2 == n:
                        res1 += 1
                        res2.append([v1, v2])
    return res1, sorted(res2, key=lambda s: s[0])


n = int(input())
res1, res2 = foo(n)
print(res1)
res3 = []
for i in res2:
    res3.extend(i)
for v in res3:
    print(v)

# def main():
#     n = 1068
#     res1,res2 = foo(n)
#     print(res1)
#     for i in res2:
#         print(i[0],i[1])
#
#
# if __name__ == '__main__':
#     a = [[0,100],[3,6],[9,8]]
#     b = sorted(a,key=lambda s:s[1])
#     print(b)
