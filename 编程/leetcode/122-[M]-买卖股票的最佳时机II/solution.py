from typing import List

# 思路：每个时刻有两种可选操作，买或卖，如果是买，看看之前卖的最大收益+当前收益，如果是卖看看之前买的最大收益和当前收益

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0]*2 for i in range(n)] # 0 buy, 1 sale
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        max_buy_profit = dp[0][0]
        max_sale_profit = dp[0][1]
        for i in range(1, n):
            dp[i][1] = max_buy_profit+prices[i]
            dp[i][0] = max_sale_profit-prices[i]
            max_buy_profit = max(max_buy_profit, dp[i][0])
            max_sale_profit = max(max_sale_profit, dp[i][1])
        max_result = 0
        for i in range(n):
            max_result = max(max_result, dp[i][1])
        return max_result


if __name__ == '__main__':
    test = Solution()
    print(test.maxProfit([7,1,5,3,6,4]))
    print(test.maxProfit([1,2,3,4,5]))
    print(test.maxProfit([7,6,4,3,1]))
    print(test.maxProfit([]))
    print(test.maxProfit([1,7,8]))