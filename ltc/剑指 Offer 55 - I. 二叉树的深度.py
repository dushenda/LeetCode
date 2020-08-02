#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 剑指 Offer 55 - I. 二叉树的深度.py
@author     : CALIBRATION
@time       : 2020/7/28 15:50
@description: None
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    depth = 0

    def maxDepth2(self, root: TreeNode) -> int:
        def get_depth(node: TreeNode, level):
            if not node:
                self.depth = max(self.depth, level)
                return
            get_depth(node.left, level + 1)
            get_depth(node.right, level + 1)

        get_depth(root, 0)
        return self.depth


def main():
    pass


if __name__ == '__main__':
    main()
