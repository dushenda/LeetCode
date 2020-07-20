#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 160. 相交链表.py
@author     : CALIBRATION
@time       : 2020/7/20 15:28
@description: None
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s = set()
        while headA:
            s.add(headA)
            headA = headA.next
        while headB and headB not in s:
            headB = headB.next
        return headB


def main():
    pass


if __name__ == '__main__':
    main()
