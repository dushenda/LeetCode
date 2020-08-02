# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    res = 0

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        def get_depth(node: TreeNode, level: int):
            if not node:
                self.res = max(self.res, level)
                return
            get_depth(node.left, level + 1)
            get_depth(node.right, level + 1)

        get_depth(root, 0)
        return self.res
