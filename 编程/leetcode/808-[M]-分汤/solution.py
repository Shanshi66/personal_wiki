# 想到N>500，返回1，就是简单dp

class Solution:
    def soupServings(self, n: int) -> float:
        N = (n//25)+1 if n%25 > 0 else n//25
        if N > 500:
            return 1
        dp = [[0 for i in range(N+1)] for j in range(N+1)]
        for i in range(N+1):
            for j in range(N+1):
                if i == 0 and j > 0:
                    dp[i][j] = 1
                elif i == 0 and j == 0:
                    dp[i][j] = 0.5
                elif j == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 0.25*(dp[max(i-4, 0)][j]+dp[max(i-3,0)][max(j-1,0)]+dp[max(i-2,0)][max(j-2,0)]+dp[max(i-1,0)][max(j-3,0)])
        return dp[N][N]

# 一种牛逼解法
class Solution:
    def soupServings(self, n: int) -> float:
        # n=4451 res=0.9999902113072541
        if n>=4500: return 1.0
        @functools.lru_cache(None) #缓存函数调用结果
        def dp(a,b):
            if a<=0 and b<=0:
                return 0.5
            elif a<=0:
                return 1.0
            elif b<=0:
                return 0.0
            else:
                return 0.25*(dp(a-100,b)+dp(a-75,b-25)+dp(a-50,b-50)+dp(a-25,b-75))
        return dp(n,n)

if __name__ == "__main__":
    test = Solution()
    # for i in range(1, 500):
        # print(i, test.soupServings(i))
    print(test.soupServings(50))
    print(test.soupServings(100))
    print(test.soupServings(1000))