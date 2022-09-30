from typing import List

# 思路1：两个标记数组，分别标识每一列、每一行是否出现0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n > 0:
            m = len(matrix[0])
        row_flag = [False]*n
        col_flag = [False]*m
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row_flag[i] = True
                    col_flag[j] = True
        for i in range(n):
            for j in range(m):
                if row_flag[i] or col_flag[j]:
                    matrix[i][j] = 0


# 思路2：两个标记变量，分别表示第一行和第一列是否出现0。用原本第一行和第一列作为思路1中的标记数组。

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_col0 = any(matrix[i][0] == 0 for i in range(m))
        flag_row0 = any(matrix[0][j] == 0 for j in range(n))
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if flag_col0:
            for i in range(m):
                matrix[i][0] = 0
        
        if flag_row0:
            for j in range(n):
                matrix[0][j] = 0

# 思路3：一个标记变量，一个变量表示第一列是否出现0，第一列第一行表示第一行是否出现0，其他同思路2
class Solution1:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_col0 = False
        
        for i in range(m):
            if matrix[i][0] == 0:
                flag_col0 = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        for i in range(m - 1, -1, -1):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if flag_col0:
                matrix[i][0] = 0

if __name__ == '__main__':
    test = Solution1()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    test.setZeroes(matrix)
    print(matrix)
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    test.setZeroes(matrix)
    print(matrix)
                    