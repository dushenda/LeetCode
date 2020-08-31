#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 剑指 Offer 52. 两个链表的第一个公共节点.py
@author     : CALIBRATION
@time       : 2020/8/31 9:41
@description: None
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # O(n) space,simple
        nums = []
        while headA:
            nums.append(headA)
            headA = headA.next
        while headB not in nums and headB:
            headB = headB.next
        return headB

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        # O(1) space and O(m+n) Time
        tmpa, tmpb = headA, headB
        while tmpa != tmpb:
            tmpa = tmpa.next if tmpa else headB
            tmpb = tmpb.next if tmpb else headA
        return tmpa


def main():
    pass


if __name__ == '__main__':
    main()
