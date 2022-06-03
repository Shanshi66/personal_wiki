from numpy import mirr


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
        max_idx = 0
        max_arm = p[0]
        for i in range(1, len(p)):
            if p[i] > max_arm:
                max_arm = p[i]
                max_idx = i
        start_idx = max_idx-max_arm
        end_idx = max_idx+max_arm
        if new_s[start_idx] == '#':
            start_idx = start_idx//2
            end_idx = (end_idx-1)//2
        else:
            start_idx = start_idx//2
            end_idx = end_idx//2
        return s[start_idx:end_idx+1]


if __name__ == '__main__':
    test = Solution()
    print(test.longestPalindrome("ababa"))
    print(test.longestPalindrome("ababaaba"))
    print(test.longestPalindrome("babad"))
    print(test.longestPalindrome("cbbd"))
    print(test.longestPalindrome("c"))
    print(test.longestPalindrome("bddb"))


