
# 思路：使用双指针，对于a,b,c,a,b,c,b,b字符串，一开始指针i指向0-a,第二个指针遍历，遍历到a发现之前出现过，就是以0-a开始的最长子串了。并且两个a之间的任意子串都是不重复，所以可以跳过验证，i指针指向1-b，j指针从3-a开始遍历。总体复杂度是O(n),因为j指针只会遍历一次字符串

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        i = 0
        j = i
        idx = {}
        ans = 1
        while i < len(s):
            for k in range(j, len(s)):
                if s[k] not in idx or idx[s[k]] == -1:
                    idx[s[k]] = k
                else:
                    ans = max(ans, k-i)
                    new_i = idx[s[k]]+1
                    idx[s[k]] = k
                    for t in range(i, new_i):
                        idx[s[t]] = -1
                    i = new_i
                    j = k
                    break
            ans = max(ans, k-i+1)
        return ans

# 更简洁的写法，方法1是以双指针中i为锚定遍历的，方法二是以j为锚定遍历。方法二想法更通畅。
# tips：这种双指针想的时候可以更换锚定试试，可能代码会更简洁

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        i = 0
        idx = {}
        ans = 1
        for j in range(0, len(s)):
            if s[j] not in idx or idx[s[j]] < i: # <i也是一种标记方法，不一定要置为true/false
                idx[s[j]] = j
                ans = max(ans, j-i+1)
            else:
                i = idx[s[j]]+1
                idx[s[j]] = j
        return ans

if __name__ == '__main__':
    test = Solution2()
    print(test.lengthOfLongestSubstring("abcabcbb"))
    print(test.lengthOfLongestSubstring("bbbb"))
    print(test.lengthOfLongestSubstring("pwwkew"))
    print(test.lengthOfLongestSubstring("w"))
    print(test.lengthOfLongestSubstring(""))
    print(test.lengthOfLongestSubstring("abcabcdbb"))
    print(test.lengthOfLongestSubstring("abcabcdbefb"))
    print(test.lengthOfLongestSubstring("au"))
    print(test.lengthOfLongestSubstring("tmmzuxt"))

            