#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 剑指 Offer 32 - I. 从上到下打印二叉树.py
@author     : CALIBRATION
@time       : 2020/7/29 15:21
@description: None
"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        deque = [root]
        res = []
        while deque:
            top = deque.pop(0)
            res.append(top.val)
            if top.left is not None: deque.append(top.left)
            if top.right: deque.append(top.right)
        return res

def main():
    pass


if __name__ == '__main__':
    main()