#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : priority_queue.py
@author     : CALIBRATION
@time       : 2020/6/28 15:53
@description: None
"""
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


def main():
    q = PriorityQueue()
    q.push(Item('foo'), 100)
    q.push(Item('bar'), -8)
    q.push(Item('spam'), 5)
    q.push(Item('grok'), 1)
    print(q.pop())
    print(q.pop())


if __name__ == '__main__':
    main()
