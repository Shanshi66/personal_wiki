from typing import List


class Solution:
    def checkRow(self, board, idx, length):
        digit = set()
        for i in range(length):
            if board[idx][i] == '.':
                continue
            if not board[idx][i] in digit:
                digit.add(board[idx][i])
            else:
                return False
        return True
    
    def checkColumn(self, board, idx, length):
        digit = set()
        for i in range(length):
            if board[i][idx] == '.':
                continue
            if not board[i][idx] in digit:
                digit.add(board[i][idx])
            else:
                return False
        return True

    def checkSquare(self, board, x, y):
        digit = set()
        for i in range(x, x+3):
            for j in range(y, y+3):
                if board[i][j] == '.':
                    continue
                if not board[i][j] in digit:
                    digit.add(board[i][j])
                else:
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)
        for i in range(length):
            if not self.checkRow(board, i, length):
                return False
            if not self.checkColumn(board, i, length):
                return False
        for i in range(3):
            for j in range(3):
                if not self.checkSquare(board, 3*i, 3*j):
                    return False
        return True


if __name__ == "__main__":
    test = Solution()
    sudo = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,["3","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

    print(test.isValidSudoku(sudo))

        