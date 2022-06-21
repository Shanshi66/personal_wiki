from typing import List


class Solution:

    def valid(self, stack):
        st = []
        for c in stack:
            if c == '(':
                st.append(c)
            elif len(st) > 0 and st[-1] == '(':                
                st.pop()
            else:
                return False
        if len(st) == 0:
            return True
        return False

    def dfs(self, result, stack, left_cnt, right_cnt):
        if left_cnt == 0 and right_cnt == 0:
            if self.valid(stack):
                result.add(''.join(stack))
                
        if left_cnt > 0:
            stack.append('(')
            left_cnt -= 1
            self.dfs(result, stack, left_cnt, right_cnt)
            left_cnt += 1
            stack.pop()
        if right_cnt > 0:
            stack.append(')')
            right_cnt -= 1
            self.dfs(result, stack, left_cnt, right_cnt)
            right_cnt += 1
            stack.pop()
        

    def generateParenthesis(self, n: int) -> List[str]:
        result = set()
        stack = []
        self.dfs(result, stack, n, n)
        return list(result)


if __name__ == '__main__':
    test = Solution()
    print(test.generateParenthesis(3))
    print(test.generateParenthesis(1))
    print(test.generateParenthesis(2))
    print(test.generateParenthesis(4))
        
        