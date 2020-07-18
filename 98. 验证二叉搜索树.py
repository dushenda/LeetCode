#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 98. 验证二叉搜索树.py
@author     : CALIBRATION
@time       : 2020/7/15 17:07
@description: None
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def is_valid(r, min, max):
            if not r: return True
            if min is not None and r.val <= min.val: return False
            if max is not None and r.val >= max.val: return False
            return is_valid(r.left, min, r) and is_valid(r.right, r, max)

        return is_valid(root, None, None)


def main():
    pass


if __name__ == '__main__':
    main()
