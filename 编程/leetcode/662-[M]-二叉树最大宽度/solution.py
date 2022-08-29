# Definition for a binary tree node.
from typing import Optional


# 思路：枚举每一层节点，根据二叉树的性质，计算序列号

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        pre = [(root, 1)]
        max_width = -1
        while pre:
            cur = []
            for node, idx in pre:
                if not node:
                    continue
                cur.append((node.left, 2*idx))
                cur.append((node.right, 2*idx+1))
            s = 0
            e = len(cur)-1
            while e >= 0 and not cur[e][0]: e -= 1
            while s < len(cur) and not cur[s][0]: s += 1
            if s <= e:
                pre = cur[s:e+1]
                max_width = max(max_width, cur[e][1]-cur[s][1]+1)
            else:
                break
        return max_width

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        pre = [(root, 1)]
        max_width = 1
        while pre:
            cur = []
            max_width = max(max_width, pre[-1][1]-pre[0][1]+1)
            for node, idx in pre:
                if node.left:
                    cur.append((node.left, 2*idx))
                if node.right:
                    cur.append((node.right, 2*idx+1))
            pre = cur
        return max_width

if __name__ == '__main__':
    test = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(8)
    root.right.right = TreeNode(7)
    root.right.right.left = TreeNode(14)
    root.right.right.right = TreeNode(7)
    print(test.widthOfBinaryTree(root))
