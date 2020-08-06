class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode):
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            pre = root.left
            while pre.right:
                pre = pre.right
            pre.right = root.right
            root.right = root.left
            root.left = None


def main():
    pass


if __name__ == '__main__':
    main()
