class Solution:
    def solve(self, s1, s2, s3, i, j, k, flag):
        if i == len(s1) and j == len(s2) and k == len(s3):
            return True
        if len(s1[i:])+len(s2[j:]) != len(s3[k:]):
            return False
        if flag == 1:
            while i < len(s1) and k < len(s3) and s3[k] == s1[i]:
                k += 1
                i += 1
                if self.solve(s1, s2, s3, i, j, k, 2):
                    return True

        if flag == 2:
            while j < len(s2) and k < len(s3) and s3[k] == s2[j]:
                k += 1
                j += 1
                if self.solve(s1, s2, s3, i, j, k, 1):
                    return True
        return False
        
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if self.solve(s1, s2, s3, 0, 0, 0, 1) or self.solve(s1, s2, s3, 0, 0, 0, 2):
            return True
        return False
        
if __name__ == '__main__':
    test = Solution()
    # print(test.isInterleave("ab", "db", "abdb"))
    # print(test.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
    # print(test.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
    # print(test.isInterleave("", "", ""))
    # print(test.isInterleave("a", "", "a"))
    print(test.isInterleave(
        "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
        "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"))