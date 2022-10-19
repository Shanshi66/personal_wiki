from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        fruit_set = {}
        i, j = 0, 0
        res = 0
        while i < n and j < n:
            if len(fruit_set) < 2 or (j < n and fruits[j] in fruit_set):
                fruit_set.setdefault(fruits[j], 0)
                fruit_set[fruits[j]] += 1
                j += 1
            else:
                res = max(res, j-i)
                k = i
                while k < n and fruits[k] == fruits[i]: 
                    fruit_set[fruits[i]] -= 1
                    k += 1
                if fruit_set[fruits[i]] == 0:
                    del fruit_set[fruits[i]]
                i = k
        res = max(res, j-i)
        return res


if __name__ == '__main__':
    test = Solution()
    print(test.totalFruit([1,2,1]))
    print(test.totalFruit([0,1,2,2]))
    print(test.totalFruit([1,2,3,2,2]))
    print(test.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))

            