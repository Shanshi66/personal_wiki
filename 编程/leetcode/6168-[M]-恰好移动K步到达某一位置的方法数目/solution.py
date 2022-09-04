from tracemalloc import start



# 思路：dp[i][j]表示花费j+1步移动到第i个坐标的方法数量
# 提前对坐标进行归一化

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        if endPos-startPos > k:
            return 0
        dp = [[0]*k for _ in range(2*k+3)]
        if startPos > endPos:
            startPos, endPos = endPos, startPos
        startPos, endPos = k+1, k+1+endPos-startPos
        dp[startPos-1][0], dp[startPos+1][0] = 1, 1
        for i in range(1, k):
            for j in range(1, 2*k+2):
                dp[j][i] = (dp[j-1][i-1]+dp[j+1][i-1])%int(1e9+7)
        return dp[endPos][k-1]


if __name__ == '__main__':
    test = Solution()
    print(test.numberOfWays(1, 2, 3))
    print(test.numberOfWays(2, 5, 10))
            

