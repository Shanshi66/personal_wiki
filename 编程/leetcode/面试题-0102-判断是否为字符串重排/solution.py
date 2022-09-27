class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        chars = {}
        for c in s1:
            chars.setdefault(c, 0)
            chars[c] += 1
        for c in s2:
            if c not in chars:
                return False
            chars[c] -= 1
            if chars[c] < 0:
                return False
        return True