#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 2. 两数相加.py
@author     : CALIBRATION
@time       : 2020/7/28 14:30
@description: None
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    carry = 0

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 加满两个链表
        tmp1, tmp2 = l1, l2
        while tmp1.next or tmp2.next:
            if not tmp1.next:
                tmp1.next = ListNode(0)
            if not tmp2.next:
                tmp2.next = ListNode(0)
            tmp1, tmp2 = tmp1.next, tmp2.next
        # 两个链表做加法
        res = ListNode(-1)
        tmp = res
        while l1 and l2:
            val = l1.val + l2.val + self.carry
            tmp.next = ListNode(val % 10)
            self.carry = val // 10
            tmp = tmp.next
            l1, l2 = l1.next, l2.next
        if self.carry > 0:
            tmp.next = ListNode(self.carry)
        return res.next


def main():
    pass


if __name__ == '__main__':
    main()
