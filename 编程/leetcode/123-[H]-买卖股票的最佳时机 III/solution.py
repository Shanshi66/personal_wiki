from turtle import left, right
from typing import List

# dp[i][j]，j=0,1,2,3表示第1,2,3,4次操作

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0]*4 for i in range(n)]
        dp[0][0]=-prices[0]; dp[0][1]=0; dp[0][2]=-prices[0]; dp[0][3]=0
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1]-prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2]+prices[i])
        max_result = max(dp[n-1][3], dp[n-1][1])
        return max_result

if __name__ == '__main__':
    test = Solution()
    print(test.maxProfit([3,3,5,0,0,3,1,4]))
    print(test.maxProfit([1,2,3,4,5]))
    print(test.maxProfit([7,6,4,3,1]))
    print(test.maxProfit([1]))