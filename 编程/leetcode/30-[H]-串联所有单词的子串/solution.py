from typing import List


# 假设单词长度是m，在某个起点，可以生成一个单词序列，用双指针枚举两端，看是否满足要求
# 起点的位置是m个，其他情况都是子问题

class Solution:
    def solve(self, word_size, word_dict, words):
        i, j = 0, 0
        result = []
        while j < len(words) and i <= j:
            if len(words)-i < word_size: # 剪枝
                break
            if j-i < word_size:
                if words[j] not in word_dict:
                    for k in range(i, j): # 把添加过的都清空
                        word_dict[words[k]] += 1
                    i = j + 1
                    j = i
                elif word_dict[words[j]] > 0:
                    word_dict[words[j]] -= 1
                    j += 1
                else:
                    word_dict[words[i]] += 1
                    i += 1
            if j-i == word_size:
                word_dict[words[i]] += 1
                result.append(i)
                i += 1
        for k in range(i, j): # 把添加过的都清空,不用copy
            word_dict[words[k]] += 1
        return result

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        size = len(words)
        if size == 0:
            return []
        n, m = len(s), len(words[0])
        if size * m > n:
            return []
        word_dict = {}
        for w in words:
            word_dict.setdefault(w, 0)
            word_dict[w] += 1
        result = []
        for i in range(m):
            split_words = [s[j:j+m] for j in range(i, n, m)]
            if len(split_words) < size:
                return []
            idx_list = self.solve(size, word_dict, split_words)
            result.extend([idx*m+i for idx in idx_list])
        return result


if __name__ == '__main__':
    test = Solution()
    print(test.findSubstring("barfoothefoobarman", ["foo","bar"]))
    print(test.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
    print(test.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
    print(test.findSubstring("barfoothe", ["bar","foo","the"]))
    print(test.findSubstring("bbarfoothe", ["bar","foo","the"]))

