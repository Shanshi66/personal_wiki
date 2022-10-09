
# 思路：将产生的数字压入栈内，模拟数字计算过程。如果栈顶是左括号，说明是(A)的形式，如果是数字，说明是AB的形式。

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack[-1] == '(':
                    stack.pop()
                    if stack and stack[-1] != '(':
                        top = stack.pop()
                        stack.append(top+1)
                    else:
                        stack.append(1)
                else:
                    top = stack.pop()
                    stack.pop()
                    if stack and stack[-1] != '(':
                        pre_top = stack.pop()
                        stack.append(pre_top+top*2)
                    else:
                        stack.append(top*2)
        return stack[0]

# 思路：计算每一个1的深度，最后的和 = 2^i+2^j+2^k+...

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = bal = 0
        for i, c in enumerate(s):
            bal += 1 if c == '(' else -1
            if c == ')' and s[i - 1] == '(':
                ans += 1 << bal
        return ans

if __name__ == '__main__':
    test = Solution()
    print(test.scoreOfParentheses("()"))
    print(test.scoreOfParentheses("(())"))
    print(test.scoreOfParentheses("()()"))
    print(test.scoreOfParentheses("(()(()))"))
