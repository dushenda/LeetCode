#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 971. 翻转二叉树以匹配先序遍历.py
@author     : CALIBRATION
@time       : 2020/9/11 8:52
@description: None
"""
from typing import List

# 抄答案的
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        self.flipped = []
        self.i = 0
        def dfs(node):
            if node:
                if node.val != voyage[self.i]:
                    self.flipped = [-1]
                    return
                self.i += 1
                if self.i < len(voyage) and node.left and node.left.val != voyage[self.i]:
                    self.flipped.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        if self.flipped and self.flipped[0] == -1:
            self.flipped = [-1]
        return self.flipped


def main():
    pass


if __name__ == '__main__':
    main()
