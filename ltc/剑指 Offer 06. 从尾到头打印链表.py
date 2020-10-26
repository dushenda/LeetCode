#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 剑指 Offer 06. 从尾到头打印链表.py
@author     : CALIBRATION
@time       : 2020/10/26 10:32
@description: None
"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        s = []
        while head:
            s.append(head.val)
            head = head.next
        return s[::-1]


def main():
    pass


if __name__ == '__main__':
    main()
