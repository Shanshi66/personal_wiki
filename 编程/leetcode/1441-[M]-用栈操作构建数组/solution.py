from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        i, j = 0, 1
        while i < len(target):
            res.append('Push')
            if j != target[i]:
                res.append('Pop')
            else:
                i += 1
            j += 1
        return res


if __name__ == '__main__':
    test = Solution()
    print(test.buildArray([1,3], 3))
    print(test.buildArray([1, 2, 3], 3))
    print(test.buildArray([1,2], 4))
    print(test.buildArray([1,5,7], 7))