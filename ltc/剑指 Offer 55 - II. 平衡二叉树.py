#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 剑指 Offer 55 - II. 平衡二叉树.py
@author     : CALIBRATION
@time       : 2020/7/28 14:29
@description: None
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     min_depth, max_depth = 10 ** 10, 0
#
#     def isBalanced(self, root: TreeNode) -> bool:
#         def get_minmax_depth(node: TreeNode, level: int):
#             if not node:
#                 self.min_depth = min(level, self.min_depth)
#                 self.max_depth = max(level, self.max_depth)
#                 return
#             get_minmax_depth(node.left, level + 1)
#             get_minmax_depth(node.right, level + 1)
#         while root:
#             get_minmax_depth(root, 0)
#             delta = self.max_depth - self.min_depth
#             if delta <= 1:
#                 return True

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(node):
            if not node:
                return 0
            left = recur(node.left)
            if left == -1:
                return -1
            right = recur(node.right)
            if right == -1:
                return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1

    # 这个更常见
    def isBalanced2(self, root: TreeNode) -> bool:
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
               self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1


def main():
    pass


if __name__ == '__main__':
    main()
