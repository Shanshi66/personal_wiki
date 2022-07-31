# 思路：贪心，从前往后遍历，碰到更优的结果就把前面字符删掉。

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        result = []
        char_cnt = {}
        used_char = set()
        for i in range(len(s)):
            char_cnt.setdefault(s[i], 0)
            char_cnt[s[i]] += 1
        for c in s:
            if c in used_char: # 如果已经用了，没有被删掉，说明存在，abca这种结构，删掉第一个a不是最优
                char_cnt[c] -= 1 # 剩余序列没有字符还有的次数，大于0的可以删，否则不行
                continue
            while result and c <= result[-1] and char_cnt[result[-1]] > 0:
                pc = result.pop()
                used_char.remove(pc)
            result.append(c)
            used_char.add(c)
            char_cnt[c] -= 1
        return ''.join(result)


if __name__ == '__main__':
    test = Solution()
    # print(test.removeDuplicateLetters('bfaf'))
    # print(test.removeDuplicateLetters('bcabc'))
    # print(test.removeDuplicateLetters('cbacdcbc'))
    # print(test.removeDuplicateLetters('cbacdcad'))
    # print(test.removeDuplicateLetters('cdacd'))
    # print(test.removeDuplicateLetters('cdadabcc'))
    print(test.removeDuplicateLetters('bbcaac'))
            