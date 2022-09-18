class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_dist = {}
        for idx, c in enumerate(s):
            char_dist.setdefault(c, [])
            char_dist[c].append(idx)
        max_dist = -1
        for c in char_dist:
            if len(char_dist[c]) >= 2:
                max_dist = max(max_dist, char_dist[c][-1]-char_dist[c][0]-1)

        return max_dist


if __name__ == '__main__':
    test = Solution()
    print(test.maxLengthBetweenEqualCharacters('abacba'))
    print(test.maxLengthBetweenEqualCharacters('aa'))
    print(test.maxLengthBetweenEqualCharacters('abca'))
    print(test.maxLengthBetweenEqualCharacters('cbzxy'))
    print(test.maxLengthBetweenEqualCharacters('cabbac'))
            