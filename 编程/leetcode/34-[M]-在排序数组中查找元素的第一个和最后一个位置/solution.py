import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        idx_left = bisect.bisect_left(nums, target)
        idx_right = bisect.bisect_right(nums, target)
        if idx_left == len(nums) or nums[idx_left] != target:
            return [-1,-1]
        else:
            return [idx_left, idx_right-1]


class Solution1:
    def bisect_right(self, nums, target):
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (right-left)//2+left
            if target >= nums[mid]:
                left = mid+1
            else:
                right = mid
        if target == nums[left]: # 只有一个元素
            left += 1
        return left

    def bisect_left(self, nums, target):
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (right-left)//2+left
            if target <= nums[mid]:
                right = mid
            else:
                left = mid+1
        return right
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        idx_left = self.bisect_left(nums, target)
        idx_right = idx_left+self.bisect_right(nums[idx_left:], target)
        if idx_left == len(nums) or nums[idx_left] != target:
            return [-1,-1]
        else:
            return [idx_left, idx_right-1]
    

if __name__ == '__main__':
    test = Solution1()
    print(test.searchRange([5,7,7,8,8,10], 8))
    print(test.searchRange([5,7,7,8,8,10], 6))
    print(test.searchRange([5,7,7,8,8,10], 7))
    print(test.searchRange([5,7,7,8,8,10], 5))
    print(test.searchRange([2,2], 5))
    print(test.searchRange([], 0))
    print(test.searchRange([1], 1))