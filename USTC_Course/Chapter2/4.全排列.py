#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 4.全排列.py
@author     : CALIBRATION
@time       : 2020/7/10 15:54
@description: None
"""


def perm(l):
    if (len(l) <= 1):
        return [l]
    r = []
    for i in range(len(l)):
        s = l[:i] + l[i + 1:]
        p = perm(s)
        for x in p:
            r.append(l[i:i + 1] + x)
    return r


def main():
    listA = [1, 2, 3]
    res = perm(listA)
    print(res)


if __name__ == '__main__':
    main()
