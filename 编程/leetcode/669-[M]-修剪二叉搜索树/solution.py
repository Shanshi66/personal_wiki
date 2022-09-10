# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from pickle import HIGHEST_PROTOCOL
from tkinter.tix import Tree
from typing import Optional


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return root
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        if low <= root.val <= high:
            return root
        if root.left:
            return root.left
        elif root.right:
            return root.right
        else:
            return None

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        print(' ', root.val, ' ')
        self.dfs(root.right)
        


if __name__ == '__main__':
    test = Solution()
    root = TreeNode(3)
    root.left = TreeNode(0)
    root.right = TreeNode(7)
    root.left.left = TreeNode(-1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(7)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(8)
    new_root = test.trimBST(root, 1, 3)
    test.dfs(new_root)