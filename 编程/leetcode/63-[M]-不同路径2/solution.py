from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n= len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(2)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i&1][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                elif j > 0:
                    dp[i&1][j] = dp[(i-1)&1][j] + dp[i&1][j-1]
                else:
                    dp[i&1][j] = dp[(i-1)&1][j]
        return dp[(m-1)&1][n-1]


test = Solution()
print(test.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(test.uniquePathsWithObstacles([[0,1],[0,0]]))
print(test.uniquePathsWithObstacles([[1,0,0],[0,1,0],[0,0,0]]))
print(test.uniquePathsWithObstacles([[1,0,0],[0,1,0],[0,0,1]]))
print(test.uniquePathsWithObstacles([[0,0,0],[0,0,0],[1,0,0]]))
print(test.uniquePathsWithObstacles([[0,0,0],[0,0,0],[0,0,0]]))