#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 206. 反转链表.py
@author     : CALIBRATION
@time       : 2020/6/29 11:04
@description: None
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 迭代
        if not head or not head.next:
            return head
        pre = head
        cur = head.next
        nex = cur.next
        pre.next = None
        while nex:
            cur.next = pre
            pre = cur
            cur = nex
            nex = nex.next
        cur.next = pre
        return cur

    def reverseList2(self, head: ListNode) -> ListNode:
        # 递归
        # 递归出口
        if not head or not head.next:
            return head
        cur = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return cur


def main():
    a = ListNode(1)
    tmp = a
    for i in range(2, 6):
        tmp.next = ListNode(i)
        tmp = tmp.next
    s = Solution()
    res = s.reverseList2(a)
    while res:
        print(res.val)
        res = res.next


if __name__ == '__main__':
    main()
