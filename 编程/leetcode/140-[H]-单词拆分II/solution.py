from asyncio import SubprocessTransport
from typing import List

# 思路：字典树+回溯，与139类似

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
    
    def generate(self, s, idx, pre, subTree):
        if idx == len(s) and ('leaf' in subTree):
            self.result.append(pre)  # 字符串遍历完，同时也要到叶子节点
            return
        if idx == len(s):
            return
        if 'leaf' in subTree:
            pre += ' '
            self.generate(s, idx, pre, self.wordTree)
            pre = pre[:-1]
        if s[idx] in subTree:
            pre += s[idx]
            self.generate(s, idx+1, pre, subTree[s[idx]])
            pre = pre[:-1]
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wordTree = self.buildTree(wordDict)
        self.result = []
        self.generate(s, 0, '', self.wordTree)
        return self.result

if __name__ == '__main__':
    test = Solution()
    print(test.wordBreak("leetcode", ["leet", "code"]))
    print(test.wordBreak("applepenapple", ["apple", "pen"]))
    print(test.wordBreak("catsandog", ["cats", "dog", "dogs", "sand", "and", "an", "cat"]))
    print(test.wordBreak("a", ["a", "aa"]))
    print(test.wordBreak("aa", ["a", "b"]))
    print(test.wordBreak("aaaaaaa", ["aaaa", "aa", "aaa"]))
    print(test.wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))
    print(test.wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))
    print(test.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
