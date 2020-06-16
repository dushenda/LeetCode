#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : 297. 二叉树的序列化与反序列化.py
@author     : CALIBRATION
@time       : 2020/6/16 15:21
@description: None
"""
import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        deque = collections.deque()
        res = []
        deque.append(root)
        res.append(str(root.val))
        while deque:
            node = deque.popleft()
            if node.left:
                deque.append(node.left)
                res.append(str(node.left.val))
            else:
                res.append('null')
            if node.right:
                deque.append(node.right)
                res.append(str(node.right.val))
            else:
                res.append('null')
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        data = data[1:-1].split(',')
        root = TreeNode(data[0])
        deque = collections.deque()
        deque.append(root)
        i = 1
        while i < len(data):
            node = deque.popleft()
            if data[i] != 'null':
                node.left = TreeNode(int(data[i]))
                deque.append(node.left)
            i += 1
            if data[i] != 'null':
                node.right = TreeNode(int(data[i]))
                deque.append(node.right)
            i += 1
        return root


def main():
    tn0 = TreeNode(1)
    tn1 = TreeNode(2)
    tn2 = TreeNode(3)
    tn3 = TreeNode(4)
    tn4 = TreeNode(5)
    tn0.left = tn1
    tn0.right = tn2
    tn2.left = tn3
    tn2.right = tn4
    c = Codec()
    res = c.serialize(tn0)
    print(res)
    print(type(res))


if __name__ == '__main__':
    main()
