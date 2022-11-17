from typing import List

# 思路：
# 1. 判断一个字符串是否为s的子序列，每个字符贪心找最前面的位置即可
# 2. 预处理s中第i个位置之后每个字符出现的最早的位置，dp[i][c]表示第i个位置开始，字符c出现的最早的位置
# 3. 判断每个字符是否是子序列的时候，遍历每个字符，去s中查找最早位置即可
# 时间复杂度O(n*26)

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        n = len(s)
        dp = [[-1]*26 for _ in range(n)]
        dp[n-1][ord(s[n-1])-ord('a')] = n-1
        for i in range(n-2, -1, -1):
            for j in range(26):
                dp[i][j] = dp[i+1][j]
            dp[i][ord(s[i])-ord('a')] = i
        res = 0
        for word in words:
            i, j = 0, 0
            while i < len(word) and j < n:
                j = dp[j][ord(word[i])-ord('a')]
                if j == -1:
                    break
                j += 1
                i += 1
            if i == len(word):
                res += 1
        return res


if __name__ == '__main__':
    test = Solution()
    print(test.numMatchingSubseq("abcde", ["a","bb","acd","ace"]))
    print(test.numMatchingSubseq("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))
    print(test.numMatchingSubseq("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax","djj"]))
    print(test.numMatchingSubseq("iwdlcxpyagegrcnrcylxolxlnhhwnxyzltiscrjztiivnpnzlubzpueihinsqdfvypdteztiodbhaqhxskupwulvkzhczdyoouym", ["hhwnxyzltiscrjztiivnpnzlubzpueihinsqdfvyp","vnpnzlubzpueihinsqdfvypdteztiodbha","rcnrcylxolxlnhhwnxyzltiscrjztiivnpnzlubzpueihi","dfvypdteztiodbhaqhxskupwulvk","zltiscrjztii","wdmbatbcewwittubryrqwwrvfkrmniomofygybeqfzusrgeart","myzfexqmzxnbmmnhmpbddqhrwrobqzjiwdzzpyzodejysuuquc","wxvrcbihbasohfvuwuxleesqeujxvjfvgwnhltenbspdgzsdrs","nztyysfhfbfcihyeaqdarqxfpjunevabzafvbmpbtenarvyizv","nivufheyodfjuggrbndyojeahrzgptikjfqufhwyhzyyjteahx"]))