# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from tkinter.tix import Tree
from turtle import left
from typing import Optional


class Solution:
    def longestUnivaluePathRoot(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root in self.root_length:
            return self.root_length[root]
        left_max = self.longestUnivaluePathRoot(root.left)
        right_max = self.longestUnivaluePathRoot(root.right)
        length = 1
        self.root_length.setdefault(root, 1)
        if root.left and root.left.val == root.val:
            length += left_max
            self.root_length[root] = max(self.root_length[root], left_max+1)
        if root.right and root.right.val == root.val:
            length += right_max
            self.root_length[root] = max(self.root_length[root], right_max+1)
        self.max_len = max(self.max_len, length)
        return self.root_length[root]

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.max_len = 0
        self.root_length = {}
        self.longestUnivaluePathRoot(root)
        return self.max_len-1


class Solution:
    def longestUnivaluePathRoot(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root in self.root_length:
            return self.root_length[root]
        left_max = self.longestUnivaluePathRoot(root.left)
        right_max = self.longestUnivaluePathRoot(root.right)
        length = 1
        max_path = 1
        if root.left and root.left.val == root.val:
            length += left_max
            max_path = max(max_path, left_max+1)
        if root.right and root.right.val == root.val:
            length += right_max
            max_path = max(max_path, right_max+1)
        self.max_len = max(self.max_len, length)
        return max_path

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.max_len = 0
        self.longestUnivaluePathRoot(root)
        return self.max_len-1


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(1)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(1)
    root.right.left.left = TreeNode(1)
    root.right.left.right = TreeNode(1)
    root.right.right.left = TreeNode(1)

    test = Solution()
    print(test.longestUnivaluePath(root))
