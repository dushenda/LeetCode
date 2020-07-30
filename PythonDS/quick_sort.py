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


def partition(array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            x += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)
    return array


import heapq


def main():
    array = [9, 7, 4, 2, 7, 5, 3]
    res = heapq.nlargest(2, array)
    print(res)
    # res = quick_sort(array, 1, len(array))
    # print(res)
    # sorted()
    # array.sort()

if __name__ == '__main__':
    main()
