#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 111. 二叉树的最小深度.py
@author     : CALIBRATION
@time       : 2020/7/20 16:09
@description: None
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        deque = [root]
        depth = 1
        while deque:
            top = deque.pop(0)
            lc = top.left
            rc = top.right
            if not lc and not rc:
                return depth
            if lc:
                deque.append(lc)
            if rc:
                deque.append(rc)
            depth += 1
        return depth


def main():
    pass


if __name__ == '__main__':
    main()
