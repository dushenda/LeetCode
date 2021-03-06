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
        def is_valid(r, minv, maxv):
            if not r: return True
            if minv is not None and r.val <= minv.val: return False
            if maxv is not None and r.val >= maxv.val: return False
            return is_valid(r.left, minv, r) and is_valid(r.right, r, maxv)

        return is_valid(root, None, None)

    def isValidBST2(self, root: TreeNode) -> bool:
        nums = []
        def traverse(r: TreeNode):
            if r is None: return
            traverse(r.left)
            nums.append(r.val)
            traverse(r.right)
        traverse(root)
        return all([nums[i]<nums[i+1] for i in range(len(nums)-1)])


def main():
    pass


if __name__ == '__main__':
    main()
