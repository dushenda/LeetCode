#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 450. 删除二叉搜索树中的节点.py
@author     : CALIBRATION
@time       : 2020/7/16 10:24
@description: None
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deleteNode(self, root: TreeNode, key: int):
        def get_tree_max(r: TreeNode):
            if r.right is None:
                return r
            return get_tree_max(r.right)

        if not root:
            return None
        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            max_Node = get_tree_max(root.left)
            root.val = max_Node.val
            root.left = self.deleteNode(root.left, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root


def main():
    pass


if __name__ == '__main__':
    main()
