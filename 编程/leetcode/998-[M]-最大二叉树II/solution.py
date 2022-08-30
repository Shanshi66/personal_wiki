# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

# 思路：附加值排在最后一定是在右边，如果比当前root值大，root所在区间在附加值左边，放到左孩子，其他情况插到右孩子。

class Solution:
    def _insertIntoMaxTree(self, root, node):
        if not root.right:
            root.right = node
            return
        if root.right.val < node.val:
            tmp = root.right
            root.right = node
            node.left = tmp
            return
        self._insertIntoMaxTree(root.right, node)
        
        
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if not root:
            return node
        if val > root.val:
            node.left = root
            return node
        self._insertIntoMaxTree(root, node)
        return root