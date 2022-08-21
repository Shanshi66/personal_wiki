from typing import List

# 字典树：先构建字段树，然后从前往后遍历，看能否在字典树上找到。

class Solution:
    def buildTree(self, wordDict):
        tree = {}
        for word in wordDict:
            p = tree
            for ch in word:
                if ch not in p:
                    p[ch] = {}
                p = p[ch]
            p['leaf'] = True # 碰到leaf有多种可能
        return tree
    
    def check(self, s, idx, subTree, fromRoot):
        if idx >= len(s) and ('leaf' in subTree or fromRoot):  # 字符串遍历完，同时也要到叶子节点
            return True
        if idx >= len(s) or s[idx] not in subTree:
            return False
        if fromRoot:
            if self.flag[idx] == 2:
                return True
            if self.flag[idx] == 1:
                return False
        if 'leaf' in subTree[s[idx]]:
            if idx+1 == len(s):
                return True
            if not self.check(s, idx+1, self.wordTree, True):
                self.flag[idx+1] = 1
            else:
                self.flag[idx+1] = 2
                return True
        return self.check(s, idx+1, subTree[s[idx]], False)
        

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordTree = self.buildTree(wordDict)
        self.flag = [0]*len(s) # 记忆化
        # print(self.wordTree)
        return self.check(s, 0, self.wordTree, fromRoot = True)


# 方法二，将字段数换成哈希set也行，使用动态规划。dp[i]表示0-i是否合法，dp[i] = dp[j] && check(i,j)
# 枚举0-之间j的位置


if __name__ == '__main__':
    test = Solution()
    print(test.wordBreak("leetcode", ["leet", "code"]))
    print(test.wordBreak("applepenapple", ["apple", "pen"]))
    print(test.wordBreak("catsandog", ["cats", "dog", "dogs", "sand", "and", "an", "cat"]))
    print(test.wordBreak("a", ["a", "aa"]))
    print(test.wordBreak("aa", ["a", "b"]))
    print(test.wordBreak("aaaaaaa", ["aaaa", "aa"]))
