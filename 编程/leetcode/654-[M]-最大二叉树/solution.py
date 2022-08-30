# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from lib2to3.pytree import Node
from typing import List, Optional


# 思路: 每次寻找一个最大值，用左区间和右区间分别构建子树。时间复杂度：T(n)=2T(n/2)+n，最理想nlogn，最坏n*n

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        max_value, max_index = nums[0], 0
        for idx, num in enumerate(nums):
            if num > max_value:
                max_value, max_index = num, idx
        root = TreeNode(max_value)
        left = self.constructMaximumBinaryTree(nums[0:max_index])
        right = self.constructMaximumBinaryTree(nums[max_index+1:])
        root.left = left
        root.right = right
        return root


# 思路：仿照leetcode998的思路，把这个看成一个插入问题，从左往右构建

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

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        root = None
        for num in nums:
            root = self.insertIntoMaxTree(root, num)
        return root


# 单调栈。如果自顶向下构建树，每次选最大值构建根，那么归属于该根的区间满足条件：左右边界都比该根要打，因为大的值优先取。因此解决问题的关键是寻找每个值的左右第一个比该元素大的元素，可以用单调栈。

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        tree = [TreeNode(x) for x in nums]
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                tree[i].left = tree[stack[-1]] # left是左边区间比i小的最大值
                stack.pop()
            if stack:
                tree[stack[-1]].right = tree[i] # right是右边区间比本身小的最大值
            stack.append(i)
        return tree[stack[0]]

