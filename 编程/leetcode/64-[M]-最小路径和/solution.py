from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n= len(grid), len(grid[0])
        dp = [[0 for i in range(n)] for j in range(2)]
        for i in range(m):
            for j in range(n):
                dp[i&1][j] = grid[i][j]
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j > 0:
                    dp[i&1][j] += dp[i&1][j-1]
                elif i > 0 and j == 0:
                    dp[i&1][j] += dp[(i-1)&1][j]
                else:
                    dp[i&1][j] += min(dp[(i-1)&1][j], dp[i&1][j-1])
        return dp[(m-1)&1][n-1]


if __name__ == '__main__':
    test = Solution()
    print(test.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
    print(test.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))