#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : quicksort2.py
@author     : CALIBRATION
@time       : 2020/8/3 22:02
@description: None
"""


def quickSort(array, l, r):
    if l >= r:
        return
    left, right = l, r
    p = array[left]
    while left < right:
        while left < right and array[right] > p:
            right -= 1
        if left < right:
            array[left] = array[right]
        while left < right and array[left] <= p:
            left += 1
        if left < right:
            array[right] = array[left]
        if left >= right:
            array[left] = p
    quickSort(array, l, right - 1)
    quickSort(array, right + 1, r)


def main():
    array = [9, 7, 7, 4, 2, 10, 5, 3]
    quickSort(array, 0, len(array) - 1)
    print(array)


if __name__ == '__main__':
    main()
