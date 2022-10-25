from typing import List

# 思路：先找到边界，然后枚举两个岛边界点对计算距离

class Solution:
    def dfs(self, grid, i, j, n, cnt, island_edge):
        if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] <= 0:
            return

        grid[i][j] = -1
        if i+1 >= n or i-1 < 0 or j+1 >= n or j-1 < 0:
            island_edge[cnt].append((i, j))
        elif grid[i+1][j] == 0 or grid[i-1][j] == 0 or \
            grid[i][j-1] == 0 or grid[i][j+1] == 0:
                island_edge[cnt].append((i, j))
        
        
        self.dfs(grid, i+1, j, n, cnt, island_edge)
        self.dfs(grid, i-1, j, n, cnt, island_edge)
        self.dfs(grid, i, j+1, n, cnt, island_edge)
        self.dfs(grid, i, j-1, n, cnt, island_edge)
        

    def shortestBridge(self, grid: List[List[int]]) -> int:
        island_edge= [[],[]]
        n = len(grid)
        cnt = -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] <= 0:
                    continue
                cnt += 1
                self.dfs(grid, i, j, n, cnt, island_edge)

        min_bridge = n+n
        for edge_a in island_edge[0]:
            for edge_b in island_edge[1]:
                min_bridge = min(min_bridge, 
                    abs(edge_a[0]-edge_b[0])+abs(edge_a[1]-edge_b[1])-1)
        return min_bridge

if __name__ == '__main__':
    test = Solution()
    print(test.shortestBridge([[0,1],[1,0]]))
    print(test.shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
    print(test.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))