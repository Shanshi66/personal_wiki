# 思路：dp[i][j]表示第i行、第j个杯子会溢出的量，当前杯子溢出的量是上一层两个杯子溢出的量-1

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        N = 100
        dp = [[0]*N for _ in range(N)]
        dp[0][0] = poured-1
        for i in range(query_row+1):
            for j in range(i+1):
                if i == 0 and j == 0:
                    continue
                if j == 0:
                    dp[i][j] = 0.5*max(dp[i-1][j], 0)-1
                elif j == i:
                    dp[i][j] = 0.5*max(dp[i-1][j-1], 0)-1
                else:
                    dp[i][j] = 0.5*max(dp[i-1][j-1], 0)+0.5*max(dp[i-1][j], 0)-1
        return min(0, dp[query_row][query_glass])+1


if __name__ == '__main__':
    test = Solution()
    print(test.champagneTower(1,1,1))
    print(test.champagneTower(2,1,1))
    print(test.champagneTower(100000009,33,17))