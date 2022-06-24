class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(2)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif j > 0:
                    dp[i&1][j] = dp[(i-1)&1][j] + dp[i&1][j-1]
                else:
                    dp[i&1][j] = dp[(i-1)&1][j]
        return dp[(m-1)&1][n-1]
    

if __name__ == "__main__":
    test = Solution()
    print(test.uniquePaths(3, 7))
    print(test.uniquePaths(3, 2))
    print(test.uniquePaths(7, 3))
    print(test.uniquePaths(3, 3))
    print(test.uniquePaths(1, 10))