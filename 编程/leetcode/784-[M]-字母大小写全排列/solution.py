from typing import List


class Solution:
    def dfs(self, idx, s, res):
        if idx == len(s):
            res.append(''.join(s))
            return
        if 'a' <= s[idx] <= 'z':
            tmp = s[idx]
            s[idx] = chr(ord('A')+ord(s[idx])-ord('a'))
            self.dfs(idx+1, s, res)
            s[idx] = tmp

        if 'A' <= s[idx] <= 'Z':
            tmp = s[idx]
            s[idx] = chr(ord('a')+ord(s[idx])-ord('A'))
            self.dfs(idx+1, s, res)
            s[idx] = tmp
        self.dfs(idx+1, s, res)
            
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        self.dfs(0, list(s), res)
        return res
    
if __name__ == '__main__':
    test = Solution()
    print(test.letterCasePermutation('a1b2'))
    print(test.letterCasePermutation('3z4'))
    print(test.letterCasePermutation('z'))