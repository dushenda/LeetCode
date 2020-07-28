#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 剑指 Offer 27. 二叉树的镜像.py
@author     : CALIBRATION
@time       : 2020/7/28 16:25
@description: None
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        tmp = root.left
        root.left = self.mirrorTree(root.right)
        root.right = self.mirrorTree(tmp)
        return root

    # 辅助栈
    def mirrorTree2(self, root: TreeNode) -> TreeNode:
        if not root: return root
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            node.left, node.right = node.right, node.left  # 交换是在栈里面交换的
        return root


def main():
    pass


if __name__ == '__main__':
    main()
