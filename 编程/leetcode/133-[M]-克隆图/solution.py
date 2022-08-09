# 思路：dfs遍历每个节点，进行复制


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def dfs_clone(self, node_set, root):
        if node_set[root.val]:
            return node_set[root.val]
        new_root = Node(val = root.val)
        node_set[root.val] = new_root
        if not root.neighbors:
            return new_root
        new_root.neighbors = []
        for i in range(len(root.neighbors)):
            new_root.neighbors.append(self.dfs_clone(node_set, root.neighbors[i]))
        return new_root

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        new_node_set = [None]*101
        new_node = self.dfs_clone(new_node_set, node)
        # print([x.val for x in new_node.neighbors])
        return new_node

if __name__ == '__main__':
    root = Node()
    root.val = 1
    root.neighbors = [Node(2), Node(3), Node(4)]
    test = Solution()
    test.cloneGraph(root)
        
        