#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : quick_sort.py
@author     : CALIBRATION
@time       : 2020/7/30 10:27
@description: None
"""


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def main():
    array = [9, 7, 7, 4, 2, 10, 5, 3]
    quick_sort(array, 0, len(array) - 1)
    print(array)


if __name__ == '__main__':
    main()
