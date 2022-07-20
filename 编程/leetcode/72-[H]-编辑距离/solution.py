
# 思路：dp[i][j]表示将word1前i个字符转成word2前j个字符的最少步数，枚举增删改各种操作
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
                    continue
                if j == 0:
                    dp[i][j] = i
                    continue
                dp[i][j] = dp[i][j-1]+1 # 增
                for k in range(1, i+1):
                    dp[i][j] = min(dp[i-k][j]+k, dp[i][j]) # 删除
                    if word2[j-1] in set(word1[i-k:i]):
                        dp[i][j] = min(dp[i-k][j-1]+k-1,dp[i][j]) #碰到相同的不用删除
                        break #只枚举到第一个相同字符地方，再往前枚举，在i=i-k的时候已经考虑过了，由此引入第二种解法
                    else:
                        dp[i][j] = min(dp[i-k][j-1]+k,dp[i][j]) # 改
        return dp[n][m]

# 思路：不用枚举k，因为之前枚举i，j的时候，k的情况已经考虑了。比如dp[i-k][j-1] 可以转移到 dp[i][j-1]，dp[i-k+1][j-1]只需要把word1[i-k]删了就行，dp[i-k+1][j-1]包含了dp[i-k][j-1]

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
                    continue
                if j == 0:
                    dp[i][j] = i
                    continue
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1 # 增、删、改
        return dp[n][m]
                

if __name__ == '__main__':
    test = Solution()
    print(test.minDistance(word1 = "horse", word2 = "ros"))
    print(test.minDistance(word1 = "intention", word2 = "execution"))
    print(test.minDistance(word1 = "i", word2 = "j"))
    print(test.minDistance(word1 = "ii", word2 = "ii"))
    print(test.minDistance(word1 = "", word2 = "ii"))
    print(test.minDistance(word1 = "iji", word2 = "ii"))
    word1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdef"
    word2 = "bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg"
    print(test.minDistance(word1, word2))