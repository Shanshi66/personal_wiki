from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        i, j = 0, 0
        n = len(nums)
        res = 0
        tmp = 0
        while i < n:
            if i == j or (j < n and nums[j] > nums[j-1]):
                tmp += nums[j]
                j += 1
            else:
                res = max(tmp ,res)
                tmp = 0
                i = j
        return res


if __name__ == '__main__':
    test = Solution()
    print(test.maxAscendingSum([10,20,30,5,10,50]))
    print(test.maxAscendingSum([10,20,30,40,50]))
    print(test.maxAscendingSum([12,17,15,13,10,11,12]))
    print(test.maxAscendingSum([100,10,1]))