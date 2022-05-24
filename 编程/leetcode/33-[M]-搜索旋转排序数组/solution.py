from typing import List

# 二分，需要判断mid在两段数组的哪一边

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (right-left)//2+left
            if target == nums[mid]:
                return mid
            elif nums[mid] > nums[right]:
                if target <= nums[right]:
                    left = mid+1
                elif target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if target < nums[mid]:
                    right = mid-1
                elif target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1


if __name__ == "__main__":
    test = Solution()
    print(test.search([4,5,6,7,0,1,2], 0))
    print(test.search([4,5,6,7,0,1,2], 3))
    print(test.search([4,5,6,7,0,1,2], 2))
    print(test.search([4,5,6,7,0,1,2], 1))
    print(test.search([4,5,6,7,0,1,2], 4))
    print(test.search([4,5,6,7,0,1], 7))
    print(test.search([4,5,6,7,0,1], 1))
    print(test.search([4,5,6,7,0,1], 6))
    print(test.search([1], 0))
    print(test.search([1], 1))
    print(test.search([1,3], 3))