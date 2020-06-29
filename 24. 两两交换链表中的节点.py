#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 24. 两两交换链表中的节点.py
@author     : CALIBRATION
@time       : 2020/6/28 16:16
@description: None
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        a = head
        b = head.next
        a.next = self.swapPairs(b.next)
        b.next = a
        return b

    def swapPairs2(self, head: ListNode) -> ListNode:
        # 非递归,三节点
        if not head or not head.next:
            return head
        dummy_head = ListNode(-1)
        dummy_head.next = head
        pre = dummy_head
        while pre and pre.next and pre.next.next:
            cur = pre.next
            nex = pre.next.next
            cur.next = nex.next
            pre.next = nex
            nex.next = cur
            pre = pre.next.next
        return dummy_head.next


def main():
    pass


if __name__ == '__main__':
    main()
