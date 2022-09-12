from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(key = lambda x: -x)
        for i in range(len(nums)):
            if i+1 == len(nums) and nums[i] >= len(nums):
                return len(nums)
            if nums[i] >= i+1 > nums[i+1]:
                return i+1
        return -1


if __name__ == '__main__':
    test = Solution()
    print(test.specialArray([3,5]))
    print(test.specialArray([0,0]))
        
