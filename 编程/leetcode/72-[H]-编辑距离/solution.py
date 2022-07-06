class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if n == 0:
            return m
        if m == 0:
            return n
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif i+1 == j:
                    dp[i][j] = dp[i][j-1]+1
                elif i-1 == j:
                    dp[i][j] = dp[i-1][j]+1
                elif word1[i-1] != word1[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = dp[i-1][j-1]
        return dp[n][m]
                

if __name__ == '__main__':
    test = Solution()
    print(test.minDistance(word1 = "horse", word2 = "ros"))
    print(test.minDistance(word1 = "intention", word2 = "execution"))