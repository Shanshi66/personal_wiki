from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        char_set = set(list(allowed))
        cnt = 0
        for word in words:
            flag = True
            for c in word:
                if not flag:
                    break
                if c not in char_set:
                    flag = False
            if flag:
                cnt += 1
        return cnt

if __name__ == '__main__':
    test = Solution()
    print(test.countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))