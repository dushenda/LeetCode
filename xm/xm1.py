#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : xm1.py
@author     : CALIBRATION
@time       : 2020/9/8 18:19
@description: None
"""

passwords = list(input().split())
res = []
tmp = [False] * 4
for iv in passwords:
    if len(iv) < 8 or len(iv) > 120:
        res.append(1)
        continue
    for ic in iv:
        if '0' <= ic <= '9': tmp[0] = True
        elif 'a' <= ic <= 'z': tmp[1] = True
        elif 'A' <= ic <= 'Z': tmp[2] = True
        else: tmp[3] = True
    if all(tmp): res.append(0)
    else: res.append(2)
    tmp = [False]*4
for r in res:
    print(r)
