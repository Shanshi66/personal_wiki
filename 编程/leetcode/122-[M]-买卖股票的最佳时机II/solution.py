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


# 官方思路：dp[i][0]表示第i天当前手上没股票的最大收益，dp[i][1]表示第i天当前手上有股票的最大收益，逻辑更顺。

# class Solution {
# public:
#     int maxProfit(vector<int>& prices) {
#         int n = prices.size();
#         int dp[n][2];
#         dp[0][0] = 0, dp[0][1] = -prices[0];
#         for (int i = 1; i < n; ++i) {
#             dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i]);
#             dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i]);
#         }
#         return dp[n - 1][0];
#     }
# };

# 状态压缩
# class Solution {
# public:
#     int maxProfit(vector<int>& prices) {
#         int n = prices.size();
#         int dp0 = 0, dp1 = -prices[0];
#         for (int i = 1; i < n; ++i) {
#             int newDp0 = max(dp0, dp1 + prices[i]);
#             int newDp1 = max(dp1, dp0 - prices[i]);
#             dp0 = newDp0;
#             dp1 = newDp1;
#         }
#         return dp0;
#     }
# };

# 思路三：贪心，找到n个不想交区间，使得sum(ri,li)=(ri,ri-1)+(ri-1,ri-2)+...+(li+1, li)最大，可以转换成找x个长度为1的区间，使价值最大。遍历每个相邻区间，取收益大于0的即可。
# class Solution {
# public:
#     int maxProfit(vector<int>& prices) {   
#         int ans = 0;
#         int n = prices.size();
#         for (int i = 1; i < n; ++i) {
#             ans += max(0, prices[i] - prices[i - 1]);
#         }
#         return ans;
#     }
# };



if __name__ == '__main__':
    test = Solution()
    print(test.maxProfit([7,1,5,3,6,4]))
    print(test.maxProfit([1,2,3,4,5]))
    print(test.maxProfit([7,6,4,3,1]))
    print(test.maxProfit([]))
    print(test.maxProfit([1,7,8]))