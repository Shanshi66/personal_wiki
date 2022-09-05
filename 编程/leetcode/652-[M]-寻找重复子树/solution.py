# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 思路：对二叉树进行序列化，序列化方式：root(left)(right),如果是空子树，也需要用()包起来

class Solution:
    def treeSerial(self, root):
        if not root:
            return ""
        tree_str = str(root.val)+"("+self.treeSerial(root.left)+")"+"("+self.treeSerial(root.right)+")"
        if tree_str in self.subTree:
            self.repeat.add(self.subTree[tree_str])
        else:
            self.subTree[tree_str] = root
        return tree_str

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        if not root:
            return []
        self.subTree = {}
        self.repeat = set()
        self.treeSerial(root)
        return list(self.repeat)


# 思路：使用(root.val, l, r)三元组序列化二叉树，其中l是左子树第一次出现序号，r是右子树第一次出现的序号。不难发现，如果l、r都重复，那么l、r必定被标记，这是如果root.val也相同，那么子树一定是重复的。
# 所有子树一定包含叶子节点，从叶子节点开始编码

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            tri = (node.val, dfs(node.left), dfs(node.right))
            if tri in seen:
                (tree, index) = seen[tri]
                repeat.add(tree)
                return index
            else:
                nonlocal idx
                idx += 1
                seen[tri] = (node, idx)
                return idx
        
        idx = 0
        seen = dict()
        repeat = set()

        dfs(root)
        return list(repeat)