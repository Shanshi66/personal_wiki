class Solution:

    def transform(self, n, base):
        b = []
        while True:
            s = n // base
            y = n % base
            b = b+[y]
            if s == 0:
                break
            n = s
        return b

    def huiwen(self, s):
        l, r = 0, len(s)-1
        while l <= r and s[l] == s[r]:
            l += 1
            r -= 1
        if l < r:
            return False
        return True

    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n-1):
            new_n = self.transform(n, base)
            # print(new_n)
            if not self.huiwen(new_n):
                return False
        return True


if __name__ == '__main__':
    test = Solution()
    print(test.isStrictlyPalindromic(9))
