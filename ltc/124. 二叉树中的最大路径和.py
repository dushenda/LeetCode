# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_len = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            cur_max = max(node.val, left + node.val, right + node.val)
            self.max_len = max(self.max_len, cur_max, node.val + left + right)

            return cur_max

        dfs(root)
        return self.max_len


def main():
    tn1 = TreeNode(5)
    tn2 = tn1.left
    if tn2:
        print(0.6)


if __name__ == '__main__':
    main()
