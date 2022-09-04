from typing import List


class Solution:

    def dfs(self, idx, cols, one_num, m, n, mat):
        if idx == n and cols > 0:
            return
        if cols == 0:
            tmp = sum([x == 0 for x in one_num])
            self.ans = max(tmp, self.ans)
            return
        for i in range(m):
            if mat[i][idx] == 1:
                one_num[i] -= 1
        self.dfs(idx+1, cols-1, one_num, m, n, mat)
        for i in range(m):
            if mat[i][idx] == 1:
                one_num[i] += 1
        self.dfs(idx+1, cols, one_num, m, n, mat)

    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        m, n = len(mat), len(mat[0])
        one_num = [0]*m
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    one_num[i] += 1
        self.ans = 0
        self.dfs(0, cols, one_num, m, n, mat)
        return self.ans


if __name__ == "__main__":
    test = Solution()
    print(test.maximumRows([[1],[0]], 1))
    print(test.maximumRows([[0,0,0],[1,0,1],[0,1,1],[0,0,1]], 2))
    print(test.maximumRows([[0,0,0],[1,0,1],[0,1,1],[0,0,1]], 1))
    print(test.maximumRows([[1,0,1],[0,0,1],[0,0,1]], 1))
