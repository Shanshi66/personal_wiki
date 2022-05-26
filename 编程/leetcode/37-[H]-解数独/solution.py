from typing import List


class Solution:
    def init(self, board):
        self.row_set = {}
        self.column_set = {}
        self.square_set = {}
        self.length = len(board)
        for i in range(self.length):
            for j in range(self.length):
                if i not in self.row_set:
                    self.row_set[i] = set()
                if i not in self.column_set:
                    self.column_set[i] = set()
                if board[i][j] != '.':
                    self.row_set[i].add(int(board[i][j]))
                if board[j][i] != '.':
                    self.column_set[i].add(int(board[j][i]))
            x = (i//3)*3
            y = (i%3)*3
            for j in range(0,3):
                for k in range(0,3):
                    if i not in self.square_set:
                        self.square_set[i] = set()
                    if board[x+j][y+k] != '.':
                        self.square_set[i].add(int(board[x+j][y+k]))

    def dfs(self, x, y, board):
        if y == self.length:
            return self.dfs(x+1, 0, board)
        if x == self.length:
            return True
        if board[x][y] == '.':
            for i in range(1, 10):
                square_idx = x//3*3+y//3
                if (i not in self.row_set[x] and 
                    i not in  self.column_set[y] and 
                    i not in self.square_set[square_idx]):
                    self.row_set[x].add(i)
                    self.column_set[y].add(i)
                    self.square_set[square_idx].add(i)
                    board[x][y] = str(i)
                    res = self.dfs(x, y+1, board)
                    if res:
                        return True
                    else:
                        self.row_set[x].remove(i)
                        self.column_set[y].remove(i)
                        self.square_set[square_idx].remove(i)
                        board[x][y] = '.'
        else:
            return self.dfs(x, y+1, board)
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """  
        self.init(board)
        self.dfs(0, 0, board)

class Solution1:
    def init(self, board):
        self.row_set = [[0]*10 for i in range(9)]
        self.column_set = [[0]*10 for i in range(9)]
        self.square_set = [[0]*10 for i in range(9)]
        self.length = len(board)
        for i in range(self.length):
            for j in range(self.length):
                if board[i][j] != '.':
                    self.row_set[i][int(board[i][j])] = 1
                if board[j][i] != '.':
                    self.column_set[i][int(board[j][i])] = 1
            x = (i//3)*3
            y = (i%3)*3
            for j in range(0,3):
                for k in range(0,3):
                    if board[x+j][y+k] != '.':
                        self.square_set[i][int(board[x+j][y+k])] = 1

    def dfs(self, x, y, board):
        if y == self.length:
            return self.dfs(x+1, 0, board)
        if x == self.length:
            return True
        if board[x][y] == '.':
            for i in range(1, 10):
                square_idx = x//3*3+y//3
                if not (self.row_set[x][i]|self.column_set[y][i]|self.square_set[square_idx][i]):
                    self.row_set[x][i]=1
                    self.column_set[y][i]=1
                    self.square_set[square_idx][i]=1
                    board[x][y] = str(i)
                    res = self.dfs(x, y+1, board)
                    if res:
                        return True
                    else:
                        self.row_set[x][i]=0
                        self.column_set[y][i]=0
                        self.square_set[square_idx][i]=0
                        board[x][y] = '.'
        else:
            return self.dfs(x, y+1, board)
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """  
        self.init(board)
        self.dfs(0, 0, board)


if __name__ == "__main__":
    test = Solution1()
    sudo = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    test.solveSudoku(sudo)
    print(sudo)

        
