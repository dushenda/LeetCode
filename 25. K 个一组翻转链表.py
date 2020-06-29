#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 25. K 个一组翻转链表.py
@author     : CALIBRATION
@time       : 2020/6/28 19:23
@description: None
"""
import collections


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    #     def trans_k(headx, k):
    #         pi = headx
    #         d = collections.deque(maxlen=k)
    #         for j in range(k):
    #             d.append(pi)
    #             pi = pi.next
    #         headx = d.pop()
    #         d.append(headx)
    #         tmp = ListNode(-1)
    #         for j in range(k):
    #             tmp.next = d.pop()
    #             tmp = tmp.next
    #         return headx
    #
    #     p, size = head, 0
    #     while p:
    #         p = p.next
    #         size += 1
    #     # 递归出口
    #     if size < k:
    #         return head
    #     # 递归条件
    #     nhead = head
    #     for i in range(k + 1):
    #         nhead = nhead.next
    #     head = trans_k(head, k)
    #     for i in range(k):
    #         head = head.next
    #     tail, head = head, head.next
    #     tail.next = self.reverseKGroup(head, k)
    #     return head

    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next

        return hair.next


def main():
    l = []
    for i in range(20):
        l.append(ListNode(i))
    for k in range(len(l) - 1):
        l[k].next = l[k + 1]
    p = l[0]
    # while p:
    #     print(p.val)
    #     p = p.next
    s = Solution()
    res = s.reverseKGroup(p, 5)
    print(res.val)


if __name__ == '__main__':
    main()
