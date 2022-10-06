# 思路：最少得括号数量等于不能匹配的括号数量，使用栈贪心匹配括号即可

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        res = 0
        for c in s:
            if c == '(':
                stack.append(c)
            elif stack:
                stack.pop()
            else:
                res += 1
        return res+len(stack)



if __name__ == '__main__':
    test = Solution()
    print(test.minAddToMakeValid("())"))
    print(test.minAddToMakeValid("((("))
    print(test.minAddToMakeValid("((()(("))
    print(test.minAddToMakeValid("((()(()"))
    print(test.minAddToMakeValid(")(()((())"))
    