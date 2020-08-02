#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 257. 二叉树的所有路径.py
@author     : CALIBRATION
@time       : 2020/7/29 16:05
@description: None
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # 当前节点是叶子节点
                    paths.append(path)  # 把路径加入到答案中
                else:
                    path += '->'  # 当前节点不是叶子节点，继续递归遍历
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root, '')
        return paths


def main():
    nums = [1, 2, 3, 5]
    tlist = [TreeNode(i) for i in nums]
    tlist[0].left = tlist[1]
    tlist[0].right = tlist[2]
    tlist[1].right = tlist[-1]
    s = Solution()
    res = s.binaryTreePaths(tlist[0])
    print(res)


if __name__ == '__main__':
    main()
