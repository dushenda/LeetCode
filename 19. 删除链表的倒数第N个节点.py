#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 19. 删除链表的倒数第N个节点.py
@author     : CALIBRATION
@time       : 2020/6/24 16:42
@description: None
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = head
        list_Node = []
        while i.next:
            list_Node.append(i)
            i = i.next
        list_Node.append(i)
        lens = len(list_Node)
        if lens == 1:
            list_Node[0] = None
        elif lens == 2:
            if n == 1:
                list_Node[0].next = None
                list_Node[1] = None
                list_Node.pop(1)
            else:
                list_Node[0] = list_Node[1]
                list_Node[1] = None
                list_Node.pop(1)
        else:
            if n == 1:
                list_Node[lens - n - 1].next = None
            else:
                list_Node[lens - n - 1].next = list_Node[lens - n + 1]
                list_Node[lens - n] = None
                list_Node.pop(lens - n)
        return list_Node[0]

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        p = head
        size = 1
        while p.next:
            size += 1
            p = p.next
        if size == 1:
            head = head.next
        else:
            if n == size:
                head = head.next
            else:
                n2 = size - n - 1
                p = head
                while n2:
                    p = p.next
                    n2 -= 1
                p.next = p.next.next
        return head


def main():
    ln1 = ListNode(1)
    ln2 = ListNode(2)
    ln3 = ListNode(3)
    ln1.next = ln2
    ln2.next = ln3
    s = Solution()
    res = s.removeNthFromEnd2(ln1, 1)
    while res.next:
        print(res.val)
        res = res.next
    print(res.val)


if __name__ == '__main__':
    main()
