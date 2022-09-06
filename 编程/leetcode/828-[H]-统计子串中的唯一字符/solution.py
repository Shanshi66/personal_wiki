from argparse import RawDescriptionHelpFormatter
import re

# 思路：先计算出总子串个数，然后删除重复字符贡献的虚假个数，超时

class Solution1:
    def uniqueLetterString(self, s: str) -> int:
        total = 0
        n = len(s)
        if n == 1:
            return 1
        for i in range(1, n+1):
            total += i*(n-i+1)

        repeat = {}
        for i in range(n):
            repeat.setdefault(s[i], [])
            repeat[s[i]].append(i)
        for c in repeat:
            if len(repeat[c]) == 1:
                continue
            repeat_n = len(repeat[c])
            for i in range(2, repeat_n+1):
                for j in range(repeat_n-i+1):
                    if j == 0 and j+i == repeat_n:
                        total -= i*(n-repeat[c][j+i-1])*(repeat[c][j]+1)
                    elif j+i == repeat_n:
                        total -= i*(repeat[c][j]-repeat[c][j-1])*(n-repeat[c][j+i-1])
                    elif j == 0:
                        total -= i*(repeat[c][j+i]-repeat[c][j+i-1])*(repeat[c][j]+1)
                    else:
                        total -= i*(repeat[c][j+i]-repeat[c][j+i-1])*(repeat[c][j]-repeat[c][j-1])
        return total

# 思路：计算每个字符的贡献，字符ci的贡献是(ci-cj)*(ck-ci)儿

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        index = {}
        for i in range(n):
            index.setdefault(s[i], [])
            index[s[i]].append(i)
        result = 0
        for c in index:
            arr = [-1]+index[c]+[n]
            for i in range(1, len(arr)-1):
                result += (arr[i]-arr[i-1])*(arr[i+1]-arr[i])
        return result

if __name__ == '__main__':
    test = Solution()
    # print(test.uniqueLetterString("ABC"))
    # print(test.uniqueLetterString("ABA"))
    print(test.uniqueLetterString("LEETCODE"))
    print(test.uniqueLetterString("LEETCODECC"))

