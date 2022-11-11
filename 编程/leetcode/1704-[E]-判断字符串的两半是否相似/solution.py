class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        alpha = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        n = len(s)
        cnt = 0
        for i in range(n//2):
            if s[i] in alpha:
                cnt += 1
        for i in range(n//2, n):
            if s[i] in alpha:
                cnt -= 1
        if cnt == 0:
            return True
        return False