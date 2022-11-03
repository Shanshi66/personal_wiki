
# 思路：二分答案

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        seq_len = len(sequence)
        word_len = len(word)
        max_repeat = seq_len//word_len
        l, r = 0, max_repeat
        while l+1 < r:
            mid = (l+r)//2
            repeat_word = word*mid
            if repeat_word in sequence:
                l = mid
            else:
                r = mid-1
        return r if word*r in sequence else l

if __name__ == '__main__':
    test = Solution()
    print(test.maxRepeating("ababc", "ab"))
    print(test.maxRepeating("ababc", "ba"))
    print(test.maxRepeating("ababc", "ac"))
    print(test.maxRepeating("aaaaa", "a"))
    print(test.maxRepeating("ababab", "ab"))
        