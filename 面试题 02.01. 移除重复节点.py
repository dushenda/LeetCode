# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        my_set = {head.val}
        ret = head
        while head.next:
            if head.next.val in my_set:
                head.next = head.next.next
            else:
                my_set.add(head.next.val)
                head = head.next
        return ret
