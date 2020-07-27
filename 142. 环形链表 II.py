#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 142. 环形链表 II.py
@author     : CALIBRATION
@time       : 2020/7/20 15:25
@description: None
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        s = set()
        while head and head not in s:
            s.add(head)
            head=head.next
        return head

def main():
    pass


if __name__ == '__main__':
    main()
