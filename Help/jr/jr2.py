#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : jr2.py
@author     : CALIBRATION
@time       : 2020/9/14 16:56
@description: None
"""

a, b = list(map(int, input().split()))
legend = [set() for _ in range(a)]
res = []
for i in range(b):
    ipts = input().split()
    order = ipts[0]
    m, n = list(map(int, ipts[1:]))
    if order == 'u':
        # 结盟
        legend[m].add(n)
        legend[n].add(m)
        for iv in legend[m]:
            for jv in legend[m]:
                legend[jv].add(iv)
        for iv in legend[n]:
            for jv in legend[n]:
                legend[jv].add(iv)
    if order == 'c':
        if n in legend[m]: res.append(1)
        else: res.append(0)

for r in res:
    print(r)
'''
4 5
u 0 1
c 0 1
u 1 2
c 0 2
c 0 3
'''


# if __name__ == '__main__':
#     s = {1,2,3,4,5,4}
#     for i in s:
#         print(i)
