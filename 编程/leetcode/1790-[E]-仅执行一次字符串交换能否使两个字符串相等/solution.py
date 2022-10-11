import enum


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff_idx = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_idx.append(i)
        if len(diff_idx) == 0:
            return True
        elif len(diff_idx) != 2:
            return False
        elif s1[diff_idx[0]] == s2[diff_idx[1]] and s2[diff_idx[0]] == s1[diff_idx[1]]:
            return True
        else:
            return False


if __name__ == '__main__':
    test = Solution()
    print(test.areAlmostEqual("bank", "kanb"))
    print(test.areAlmostEqual("attack", "defend"))
    print(test.areAlmostEqual("kelb", "kelb"))
    print(test.areAlmostEqual("abcd", "dcba"))
        