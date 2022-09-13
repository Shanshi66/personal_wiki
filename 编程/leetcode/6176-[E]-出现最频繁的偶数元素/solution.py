from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num&1:
                continue
            freq.setdefault(num, 0)
            freq[num] += 1
        if not freq:
            return -1
        freq_list = list(freq.items())
        freq_list.sort(key = lambda x: (-x[1], x[0]))
        return freq_list[0][0]



if __name__ == '__main__':
    test = Solution()
    print(test.mostFrequentEven([0,1,2,2,4,4,1]))
    print(test.mostFrequentEven([4,4,4,9,2,4]))
    print(test.mostFrequentEven([29,47,21,41,13,37,25,7]))


                