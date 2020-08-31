#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 剑指 Offer 54. 二叉搜索树的第k大节点.py
@author     : CALIBRATION
@time       : 2020/8/31 15:19
@description: None
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # O(n) Space
        nums = []

        def tranverse(root: TreeNode):
            if not root: return
            tranverse(root.right)
            nums.append(root.val)
            tranverse(root.left)

        tranverse(root)
        return nums[k - 1]

    def kthLargest2(self, root: TreeNode, k: int) -> int:
        # O(1) Space
        def dfs(root: TreeNode):
            if not root: return
            dfs(root.right)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0: self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res


def main():
    pass


if __name__ == '__main__':
    main()
