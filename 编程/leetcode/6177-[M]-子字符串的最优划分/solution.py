class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        char_set = set()
        for c in s:
            if c not in char_set:
                char_set.add(c)
            else:
                count += 1
                char_set = set()
                char_set.add(c)
        count += 1
        return count


if __name__ == '__main__':
    test = Solution()
    print(test.partitionString("abacaba"))
    print(test.partitionString("ssssss"))
    print(test.partitionString("abbcbaa"))
    print(test.partitionString("a"))