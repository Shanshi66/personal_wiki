from typing import List

# 思路：用单调栈求预处理每个1的上左右最大边界，在求下边界的时候，求最大十字


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        left = [[0]*n for _ in range(n)]
        right = [[0]*n for _ in range(n)]
        up = [[0]*n for _ in range(n)]
        ans = 0
        new_mines = [[1]*n for _ in range(n)]
        for pair in mines:
            new_mines[pair[0]][pair[1]] = 0
        for i in range(n):
            st = []
            bound = -1
            for j in range(n):
                while st and new_mines[i][j] == 0:
                    right[i][st[-1]] = j
                    st.pop()
                if new_mines[i][j] == 1:
                    st.append(j)
                    left[i][j] = bound
                else:
                    bound = j
            while st:
                right[i][st[-1]] = n
                st.pop()
        for i in range(n):
            st = []
            bound = -1
            for j in range(n):
                while st and new_mines[j][i] == 0:
                    tmp = min(j-st[-1], st[-1]-up[st[-1]][i], 
                        i-left[st[-1]][i], right[st[-1]][i]-i)
                    ans = max(tmp, ans)
                    st.pop()
                if new_mines[j][i] == 1:
                    st.append(j)
                    up[j][i] = bound
                else:
                    bound = j
            while st:
                tmp = min(n-st[-1], st[-1]-up[st[-1]][i], 
                    i-left[st[-1]][i], right[st[-1]][i]-i)
                ans = max(tmp, ans)
                st.pop()
        return ans


if __name__ == '__main__':
    test = Solution()
    print(test.orderOfLargestPlusSign(5, [[4, 2]]))
    print(test.orderOfLargestPlusSign(2, [[0, 0]]))
    print(test.orderOfLargestPlusSign(3, [[1,1]]))
    print(test.orderOfLargestPlusSign(1, []))