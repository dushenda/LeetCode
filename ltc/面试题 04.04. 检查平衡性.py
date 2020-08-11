#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 面试题 04.04. 检查平衡性.py
@author     : CALIBRATION
@time       : 2020/8/11 16:12
@description: None
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isBalanced(self, root: TreeNode) -> bool:
        # 递归求深度，会造成重复计算
        def get_depth(node: TreeNode) -> int:
            if not node:
                return 0
            return max(get_depth(node.left), get_depth(node.right)) + 1

        if not root: return True
        if abs(get_depth(root.left) - get_depth(root.right)) > 1: return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    flag = True

    def isBalanced2(self, root: TreeNode) -> bool:
        def dfs(node: TreeNode) -> int:
            if not node or not self.flag:
                return 0
            left_depth = dfs(node.left) + 1
            right_depth = dfs(node.right) + 1
            if abs(left_depth - right_depth) > 1:
                self.flag = False
            return max(left_depth, right_depth)
        dfs(root)
        return self.flag


def main():
    pass


if __name__ == '__main__':
    main()
