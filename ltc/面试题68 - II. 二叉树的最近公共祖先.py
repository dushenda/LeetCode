#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 面试题68 - II. 二叉树的最近公共祖先.py
@author     : CALIBRATION
@time       : 2020/7/29 15:33
@description: None
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 最近公共祖先的定义： 设节点 rootroot 为节点 p, qp,q 的某公共祖先，若其左子节点 root.leftroot.left 和右子节点 root.rightroot.right 都不是 p,qp,
# q 的公共祖先，则称 rootroot 是 “最近的公共祖先” 。


# 递归解析：
# 终止条件：
# 当越过叶节点，则直接返回 nullnull ；
# 当 rootroot 等于 p, qp,q ，则直接返回 rootroot ；
# 递推工作：
# 开启递归左子节点，返回值记为 leftleft ；
# 开启递归右子节点，返回值记为 rightright ；
# 返回值： 根据 leftleft 和 rightright ，可展开为四种情况；
# 当 leftleft 和 rightright 同时为空 ：说明 rootroot 的左 / 右子树中都不包含 p,qp,q ，返回 nullnull ；
# 当 leftleft 和 rightright 同时不为空 ：说明 p, qp,q 分列在 rootroot 的 异侧 （分别在 左 / 右子树），因此 rootroot 为最近公共祖先，返回 rootroot ；
# 当 leftleft 为空 ，rightright 不为空 ：p,qp,q 都不在 rootroot 的左子树中，直接返回 rightright 。具体可分为两种情况：
# p,qp,q 其中一个在 rootroot 的 右子树 中，此时 rightright 指向 pp（假设为 pp ）；
# p,qp,q 两节点都在 rootroot 的 右子树 中，此时的 rightright 指向 最近公共祖先节点 ；
# 当 leftleft 不为空 ， rightright 为空 ：与情况 3. 同理；

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root


def main():
    pass


if __name__ == '__main__':
    main()
