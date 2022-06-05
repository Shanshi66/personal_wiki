from numpy import mirr

# 马拉车：在字符之间填充#，使得所有字符串长度都是奇数。记录能识别到的最右边界maxRight，及对应的center。遍历每一个字符，考虑center左边对称位置的回文串臂长，如果当前位置+臂长没有超过maxRight，直接继承计算结果，否则从maxRight开始逐步向外扩展，更新maxRight和center。

class Solution:
    def expand(self, new_s, i, j):
        while i >= 0 and j < len(new_s) and new_s[i] == new_s[j]:
            i -= 1
            j += 1
        return j-1

    def longestPalindrome(self, s: str) -> str:
        max_right = 2
        center = 1
        new_s = '#'+'#'.join(list(s))+'#'
        p = [0]*len(new_s)
        p[1] = 1
        start, end = 0, 0
        for i in range(1, len(new_s)):
            mirror = 2*center-i
            if i > max_right:
                max_right = self.expand(new_s, i, i)
                center = i
                p[i] = max_right-i
            elif i+p[mirror] < max_right:
                p[i] = p[mirror]
            else:
                max_right = self.expand(new_s, i-(max_right-i), max_right)
                center = i
                p[i] = max_right-i
            if 2*p[i] > end-start:
                start = i-p[i]
                end = i+p[i]
        return new_s[start+1:end+1:2]


if __name__ == '__main__':
    test = Solution()
    print(test.longestPalindrome("ababa"))
    print(test.longestPalindrome("ababaaba"))
    print(test.longestPalindrome("babad"))
    print(test.longestPalindrome("cbbd"))
    print(test.longestPalindrome("c"))
    print(test.longestPalindrome("bddb"))
    print(test.longestPalindrome("babadada"))


