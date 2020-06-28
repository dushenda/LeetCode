#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : Tdeque.py
@author     : CALIBRATION
@time       : 2020/6/28 15:31
@description: None
"""
import collections
import heapq


def main():
    d = collections.deque(maxlen=5)
    for i in range(10):
        d.append(i)
    print(d)
    print("===============")
    l = [3, 5, 6, 8, 9, 1, 23, 100, 2, 5]
    heapq.heapify(l)
    print(l)
    print(heapq.heappop(l))
    print(l)
    heapq.heappush(l, 900)
    print(l)


if __name__ == '__main__':
    main()
