from collections import deque
from enum import Flag
import functools
from typing import List

# 最小高度树的根一定在最长路径上，且是中点(如果路径长度为奇数是中点，如果是偶数，中间的pair都可以作为根)。可以反证法证明，如果不是，有两种情况，1）根在最长路径上，但不在中点上，那么根节点与最长路径远端的距离一定大于最长路径的一半；2）根不在最长路径上，根到叶子节点必定要与最长路径有交点，那么最小高度一定比最长路径的一半要长
# 拓扑排序：依次删除度为1的点，剩下的位最长路径下剩余的点
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]
        graph = {}
        degree = [0]*n
        for edge in edges:
            graph.setdefault(edge[0], []).append(edge[1])
            graph.setdefault(edge[1], []).append(edge[0])
            degree[edge[0]] += 1
            degree[edge[1]] += 1

        node_left = n
        delete = [False]*n

        delete_node = []
        for i in range(n):
            if degree[i] == 1:
                delete_node.append(i)
                delete[i] = True
                node_left -= 1
        
        while node_left > 2:
            tmp = []
            for node in delete_node:
                for son in graph[node]:
                    if delete[son]:
                        continue
                    degree[son] -= 1
                    if degree[son] == 1:
                        tmp.append(son)
                        delete[son] = True
                        node_left -= 1
            delete_node = tmp
        result = set()
        for node in delete_node:
            for son in graph[node]:
                if not delete[son]:
                    result.add(son)
        return list(result)

# 也可以先找出最长路径，再取路径中点
# 求最长路径的方法：以任意顶点p出发，找距离最远的顶点x，以x出发，找距离x最远的顶点y，xy为最长路径

if __name__ == '__main__':
    test = Solution()
    print(test.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
    print(test.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
    print(test.findMinHeightTrees(1, []))
    print(test.findMinHeightTrees(2, [[0,1]]))
    print(test.findMinHeightTrees(3, [[0,1], [0,2]]))

        

        
            
            