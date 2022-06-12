
# 这种边界很复杂的，按正确的逻辑去实现是最安全的

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0 and len(p) == 0:
            return True
        if len(p) == 0 and len(s) > 0:
            return False
        if len(p) > 1 and p[1] == '*': 
            next_p = 2
            while next_p < len(p) and p[next_p] == '*': next_p += 1
            for i in range(len(s)+1):
                if p[0] == '.' or i == 0:
                    if self.isMatch(s[i:], p[next_p:]):
                        return True
                elif s[i-1] != p[0]:
                    break
                elif self.isMatch(s[i:], p[next_p:]):
                    return True
        elif len(s) == 0 and len(p) > 0:
            return False
        elif (p[0] == '.' or p[0] == s[0]) and self.isMatch(s[1:], p[1:]):
            return True
        return False


if __name__ == "__main__":
    test = Solution()
    print(test.isMatch('aa', 'a'))
    print(test.isMatch('aa', 'a*'))
    print(test.isMatch('aa', '.*'))
    print(test.isMatch('aabcesdesfs', '.*s'))
    print(test.isMatch('aabcesdesfs', '.*d'))
    print(test.isMatch('aabcesdesfs', '.*.'))
    print(test.isMatch('aabcesdesfs', '.***.'))
    print(test.isMatch('a', '.'))
    print(test.isMatch('aab', 'c*a*b')) ## 陷阱，*可以匹配0个
    print(test.isMatch('a', 'ab*')) 
    print(test.isMatch('a', 'a*'))
    print(test.isMatch('a', '.*..a*')) 
    print(test.isMatch("mississippi", "mis*is*p*."))
