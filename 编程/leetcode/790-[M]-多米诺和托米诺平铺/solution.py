
# 思路：状态dp，在第i个位置，有四种情况：1）两个都为空；2,3）其中一个为空；4)两个都填满。根据这个进行状态转移。

class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [[0]*4, [0]*4]
        dp[0][0], dp[0][1], dp[0][2], dp[0][3] = 1, 0, 0, 1
        mod = int(1e9+7)
        for i in range(1, n):
            cur, pre = i%2, (i-1)%2
            dp[cur][0] = dp[pre][3]
            dp[cur][1] = (dp[pre][2]+dp[pre][0])%mod
            dp[cur][2] = (dp[pre][1]+dp[pre][0])%mod
            dp[cur][3] = (dp[pre][3]+dp[pre][1]+dp[pre][2]+dp[pre][0])%mod # 加上dp[pre][0]是考虑把两个横的情况考虑进来
        return dp[(n-1)%2][3]


if __name__ == '__main__':
    test = Solution()
    print(test.numTilings(3))
    print(test.numTilings(1))