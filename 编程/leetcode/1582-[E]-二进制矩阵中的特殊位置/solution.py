from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        rows = [0]*n
        for i in range(n):
            one_num = 0
            for j in range(m):
                if mat[i][j] == 1:
                    one_num += 1
            rows[i] = one_num
        result = 0
        for j in range(m):
            one_num = 0
            for i in range(n):
                if mat[i][j] == 1:
                    one_num += 1
                    idx = i
            if one_num == 1 and rows[idx] == 1:
                result += 1
        return result

    
if __name__ == '__main__':
    test = Solution()
    print(test.numSpecial([[1,0,0],[0,0,1],[1,0,0]]))
    print(test.numSpecial([[1,0,0],[0,1,0],[0,0,1]]))
    print(test.numSpecial([[0,0,0,1],[1,0,0,0],[0,1,1,0],[0,0,0,0]]))