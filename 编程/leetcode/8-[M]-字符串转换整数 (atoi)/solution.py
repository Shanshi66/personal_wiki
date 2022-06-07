
# TIPS：边界情况一定要小心，特别是while循环里的index

class Solution:
    def is_digit(self, c):
        if c >= '0' and c <= '9':
            return True
        return False
    
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = 0
        while i < len(s) and s[i] == ' ': i += 1
        if i == len(s):
            return 0
        is_pos = False if s[i] == '-' else True
        if s[i] == '-' or s[i] == '+':
            start, end = i+1, i+1
        else:
            start, end = i, i
        
        if start < len(s) and self.is_digit(s[start]):
            while end < len(s) and self.is_digit(s[end]):end += 1
        else:
            return 0
        
        num = 0
        for i in range(start, end):
            num = num*10+int(s[i])
        num = num if is_pos else -num
        num = max(num, -2**31) if num < 0 else min(num, 2**31-1)
        return num

if __name__ == "__main__":
    test = Solution()
    print(test.myAtoi("112"))
    print(test.myAtoi("+112"))
    print(test.myAtoi("-112"))
    print(test.myAtoi("    -112"))
    print(test.myAtoi("    -  112"))
    print(test.myAtoi("    -11111111111111111111111111111"))
    print(test.myAtoi("4193   swe"))
    print(test.myAtoi("41.93   swe"))
    print(test.myAtoi(""))
    print(test.myAtoi("+"))
    print(test.myAtoi("++"))
    print(test.myAtoi(" "))
    print(test.myAtoi("   "))