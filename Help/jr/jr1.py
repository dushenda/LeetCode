#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : jr1.py
@author     : CALIBRATION
@time       : 2020/9/14 16:37
@description: None
"""
n = int(input())
nums = []
for i in range(n):
    tmp = float(input())
    nums.append(tmp)
res = []
for i in range(1, n + 1):
    tmp = sorted(nums[:i])
    if i & 1:
        res.append(tmp[(i + 1) // 2 - 1])
    else:
        res.append(tmp[i // 2 - 1])
for r in res:
    print(r)


'''
5
0.01
5.00
55.00
4.00
999.99
'''
