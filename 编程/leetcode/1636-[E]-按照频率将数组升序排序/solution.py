from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq.setdefault(num, 0)
            freq[num] += 1
        nums.sort(key = lambda x: (freq[x], -x))
        return nums
    


if __name__ == '__main__':
    test = Solution()
    print(test.frequencySort([1,1,2,2,2,3]))
    print(test.frequencySort([2,3,1,3,2]))
    print(test.frequencySort([-1,1,-6,4,5,-6,1,4,1]))