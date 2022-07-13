from typing import List

# 思路：枚举每一行，枚举每一个连续为1的序列，看以这个序列为边的最大矩形面积

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        if m == 0:
            return 0
        dp = [[[0]*m for i in range(m)], [[0]*m for i in range(m)]]
        max_result = 0
        for i in range(n):
            dp[i&1] = [[0]*m for i in range(m)]
            for j in range(0, m):
                if matrix[i][j] == '0':
                    continue
                for k in range(j, m):
                    if matrix[i][k] == '0':
                        break
                    dp[i&1][j][k] = dp[(i-1)&1][j][k] + k-j+1
                    max_result = max(max_result, dp[i&1][j][k])
        return max_result

if __name__ == '__main__':
    test = Solution()
    print(test.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    print(test.maximalRectangle([]))
    print(test.maximalRectangle([['0']]))
    print(test.maximalRectangle([['1']]))
    print(test.maximalRectangle([['1', '1']]))
    print(test.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","0"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    print(test.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","0"],["1","1","0","1","1"],["1","0","0","1","0"]]))
    print(test.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","0"],["1","1","0","1","1"],["1","0","0","1","0"],["1","0","0","1","0"]]))
