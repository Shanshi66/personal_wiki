class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_set = {}
        for c in s:
            char_set.setdefault(c, 0)
            char_set[c] += 1
        res = ''
        for c in order:
            if c not in char_set:
                continue
            res += c*char_set[c]
            char_set[c] = 0
        for c in char_set:
            res += c*char_set[c]
        return res

    
if __name__ == '__main__':
    test = Solution()
    print(test.customSortString("cba", "abcd"))
    print(test.customSortString("cbafg", "ffggaabcd"))
    print(test.customSortString("hucw", "utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"))