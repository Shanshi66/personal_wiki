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

# 思路：对于第i行来说，使用dp[i][j]表示位置j的最长1的高度，问题转变成了在一个柱状图里寻找最大面积矩形。具体思路参见leetcode84。

class Solution1:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        if m == 0:
            return 0
        dp = [[0]*m for i in range(2)]
        max_result = 0
        for i in range(n):
            for j in range(m):
                dp[i&1][j] = 1+dp[(i-1)&1][j] if matrix[i][j] == '1' else 0
            stack = []
            left = [0]*m
            right = [m]*m
            for j in range(m):
                while stack and dp[i&1][j] <= dp[i&1][stack[-1]]:
                    right[stack[-1]] = j
                    stack.pop()
                left[j] = stack[-1] if stack else -1
                stack.append(j)
            for j in range(m):
                max_result = max(max_result, (right[j]-left[j]-1)*dp[i&1][j])
        return max_result

if __name__ == '__main__':
    test = Solution1()
    print(test.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    print(test.maximalRectangle([]))
    print(test.maximalRectangle([['0']]))
    print(test.maximalRectangle([['1']]))
    print(test.maximalRectangle([['1', '1']]))
    print(test.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","0"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    print(test.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","0"],["1","1","0","1","1"],["1","0","0","1","0"]]))
    print(test.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","0"],["1","1","0","1","1"],["1","0","0","1","0"],["1","0","0","1","0"]]))
