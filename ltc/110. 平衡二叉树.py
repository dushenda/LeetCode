# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        return abs(self.get_depth(root.left) - self.get_depth(root.right)) <= 1 and \
               self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_depth(self, node: TreeNode) -> int:
        if not node: return 0
        return max(self.get_depth(node.left), self.get_depth(node.right)) + 1


class SolutionBetter:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.recur(root) != -1

    def recur(self, root):
        if not root: return 0
        left = self.recur(root.left)
        if left == -1: return -1
        right = self.recur(root.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1
