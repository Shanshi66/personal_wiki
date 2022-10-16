from re import sub
from typing import List


# 思路：二部图判断，染色法。当前人分在第一组，不喜欢的分第二组，如果有冲突就不能分。

class Solution:

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        classify = [0]*(n+1)

        edges = {}
        for edge in dislikes:
            edges.setdefault(edge[0], set())
            edges[edge[0]].add(edge[1])
            edges.setdefault(edge[1], set())
            edges[edge[1]].add(edge[0])

        def dfs(node, color):
            classify[node] = color
            if node not in edges:
                return True
            flag = True
            for subnode in edges[node]:
                if not flag:
                    break
                if classify[subnode] == color:
                    flag = False
                elif classify[subnode] == 0:
                    flag = dfs(subnode, -color)
                else:
                    continue
            return flag

        flag2 = True
        for i in range(1,1+n):
            if not flag2:
                return False
            if not classify[i]:
                flag2 = dfs(i, 1)
        return True


if __name__ == '__main__':
    test = Solution()
    print(test.possibleBipartition(4, [[1,2],[1,3],[2,4]]))
    print(test.possibleBipartition(3, [[1,2],[1,3],[2,3]]))
    print(test.possibleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]]))