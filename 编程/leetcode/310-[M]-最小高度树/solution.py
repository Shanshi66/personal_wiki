from collections import deque
import functools
from typing import List


# class Solution:
#     # def solve(self, dp, u, v):
#     #     if dp[u][v] != -1:
#     #         return dp[u][v]
#     #     for w in dp[v]:
#     #         if w == u:
#     #             continue
#     #         dp[u][v] = max(dp[u][v], self.solve(dp, v, w)+1)
#     #     if dp[u][v] == -1:
#     #         dp[u][v] = 0
#     #     return dp[u][v]

#     def solve(self, dp, u, v):
#         if dp[u][v] != -1:
#             return dp[u][v]
#         stack = [(u, v)]
#         while stack:
#             _u, _v = stack[-1]
#             if not dp[_v]:
#                 dp[_u][_v] = 1
#                 stack.pop()
#                 continue
#             for s in dp[_v]:
#                 if _u == s:
#                     continue
#                 if dp[_v][s] == -1:
#                     stack.append((_v, s))
#                 else:
#                     dp[_u][_v] = max(dp[_u][_v], dp[_v][s]+1)
            
            
                
            

#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         dp = {}
#         for edge in edges:
#             dp.setdefault(edge[0], {})
#             dp.setdefault(edge[1], {})
#             dp[edge[0]][edge[1]] = -1
#             dp[edge[1]][edge[0]] = -1
#         result = {}
#         min_height = n
#         for u in dp:
#             height_ = -1
#             for v in dp[u]:
#                 dp[u][v] = self.solve(dp, u, v)
#                 height_ = max(height_, dp[u][v])
#             min_height = min(height_, min_height)
#             result.setdefault(height_, []).append(u)
#         if min_height == n:
#             return [0]
#         return result[min_height]

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        parents = [0] * n

        def bfs(start: int):
            vis = [False] * n
            vis[start] = True
            q = deque([start])
            while q:
                x = q.popleft()
                for y in g[x]:
                    if not vis[y]:
                        vis[y] = True
                        parents[y] = x
                        q.append(y)
            return x
        x = bfs(0)  # 找到与节点 0 最远的节点 x
        y = bfs(x)  # 找到与节点 x 最远的节点 y

        path = []
        parents[x] = -1
        while y != -1:
            path.append(y)
            y = parents[y]
        m = len(path)
        print(path)
        return [path[m // 2]] if m % 2 else [path[m // 2 - 1], path[m // 2]]


if __name__ == '__main__':
    test = Solution()
    # print(test.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
    print(test.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
    # print(test.findMinHeightTrees(1, []))

        

        
            
            