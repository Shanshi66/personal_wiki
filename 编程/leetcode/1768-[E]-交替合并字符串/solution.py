class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        i = 0
        res = ''
        while i < n and i < m:
            res += word1[i]
            res += word2[i]
            i += 1
        if i < n:
            res += word1[i:]
        if i < m:
            res += word2[i:]
        return res

if __name__ == '__main__':
    test = Solution()
    print(test.mergeAlternately("abc", "pqr"))
    print(test.mergeAlternately("ab", "pqrs"))
    print(test.mergeAlternately("abcd", "pq"))