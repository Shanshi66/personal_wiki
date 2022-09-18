from typing import List


class Solution:
    def dfs(self, grid, x, y, visit, flag):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid):
            return
        if grid[x][y] == 0 or visit[x][y]:
            return
        visit[x][y] = flag
        self.area.setdefault(flag, 0)
        self.area[flag] += 1
        self.dfs(grid, x+1, y, visit, flag)
        self.dfs(grid, x-1, y, visit, flag)
        self.dfs(grid, x, y-1, visit, flag)
        self.dfs(grid, x, y+1, visit, flag)

    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = [[0]*n for _ in range(n)]
        count = 0
        self.area = {}
        for i in range(n):
            for j in range(n):
                if visit[i][j] or grid[i][j] == 0:
                    continue
                count += 1
                self.dfs(grid, i, j, visit, count)
        if not self.area:
            return 1
        if self.area[1] == n*n:
            return n*n
        
        max_area = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    continue
                flag_set = set()
                if i-1 >= 0 and visit[i-1][j]:
                    flag_set.add(visit[i-1][j])
                if i+1 < n and visit[i+1][j]:
                    flag_set.add(visit[i+1][j])
                if j-1 >= 0 and visit[i][j-1]:
                    flag_set.add(visit[i][j-1])
                if j+1 < n and visit[i][j+1]:
                    flag_set.add(visit[i][j+1])
                if not flag_set:
                    continue
                sum_area = 1
                for flag in flag_set:
                    sum_area += self.area[flag]
                max_area = max(max_area, sum_area)
        return max_area

if __name__ == '__main__':
    test = Solution()
    print(test.largestIsland([[1, 0], [0, 1]]))
    print(test.largestIsland([[1, 1], [1, 0]]))
    print(test.largestIsland([[1, 1], [1, 1]]))
                