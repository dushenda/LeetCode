#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : heapqs.py
@author     : CALIBRATION
@time       : 2020/9/9 15:20
@description: None
"""


def parent(i): return (i - 1) // 2


def left(i): return 2 * i + 1


def right(i): return 2 * i + 2


def heapifys(A, i):
    l, r = left(i), right(i)
    if l < len(A) and A[l] < A[i]:
        largest = l
    else:
        largest = i
    if r < len(A) and A[r] < A[largest]: largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapifys(A, largest)


def build_heap(A):
    for i in range(len(A) // 2, -1, -1):
        heapifys(A, i)


def heapq_sort(A):
    res = []
    lens = len(A)
    for i in range(lens):
        res.append(A.pop(0))
        heapifys(A, 0)
    return res


def main():
    import heapq
    nums = [1, 3, 4, 6, 7, 3, 2, 5]
    res = heapq_sort(nums)
    print(res)
    # nums2 = nums.copy()
    # heapq.heapify(nums2)
    # build_heap(nums)
    # print(nums)
    # print(nums2)


if __name__ == '__main__':
    main()
