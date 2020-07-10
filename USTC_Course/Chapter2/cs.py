#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : cs.py
@author     : CALIBRATION
@time       : 2020/7/10 16:56
@description: None
"""


def perm(A):
    if len(A) == 1:
        return [A]
    r = []
    for i in range(len(A)):
        get = A[i]
        resi = A[:i] + A[i + 1:]
        res = perm(resi)
        for j in res:
            r.append([get] + j)
    return r


def main():
    A = [1, 2, 3, 4]
    res = perm(A)
    print(res)


if __name__ == '__main__':
    main()
