#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 剑指 Offer 09. 用两个栈实现队列.py
@author     : CALIBRATION
@time       : 2020/6/30 11:22
@description: None
"""
import collections


class CQueue:

    def __init__(self):
        self.stack1 = collections.deque()
        self.stack2 = collections.deque()

    def appendTail(self, value: int) -> None:
        self.stack2.append(value)

    def deleteHead(self) -> int:
        if not self.stack1 and not self.stack2:
            return -1
        # move 2 to 1
        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
        return self.stack1.pop()


def main():
    value = 'CQueue'
    obj = CQueue()
    obj.appendTail(value)
    param_2 = obj.deleteHead()


if __name__ == '__main__':
    main()
