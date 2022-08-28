from typing import List
import sys


class Solution1:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [x-1 for x in nums]
        nums.sort()
        if nums[-2] > 0:
            return nums[-1]*nums[-2]
        return nums[0]*nums[1]


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_1, max_2 = -1, -1
        for n in nums:
            if n >= max_1:
                max_2 = max_1
                max_1 = n
            elif n >= max_2:
                max_2 = n
            else:
                continue
        return (max_1-1)*(max_2-1)

if __name__ == '__main__':
    test = Solution()
    print(test.maxProduct([3,4,5,2]))
    print(test.maxProduct([1,5,4,5]))
    print(test.maxProduct([3,7]))
    print(test.maxProduct([1,1,1,1]))
    print(test.maxProduct([10,2,5,2]))
