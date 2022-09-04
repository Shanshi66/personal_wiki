from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        word_dis = {}
        lib = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i, c in enumerate(s):
            if c not in word_dis:
                word_dis[c] = i
            else:
                word_dis[c] = abs(word_dis[c]-i)-1
        for i in range(len(distance)):
            c = lib[i]
            if c not in word_dis:
                continue
            if distance[i] != word_dis[c]:
                return False

        return True


if __name__ == '__main__':
    test = Solution()
    print(test.checkDistances('abaccb', [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
    print(test.checkDistances('aa', [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))

