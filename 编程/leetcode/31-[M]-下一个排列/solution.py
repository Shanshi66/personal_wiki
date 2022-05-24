from bisect import bisect_right
import bisect
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        break
                nums[i-1], nums[j] = nums[j], nums[i-1]
                nums[i:] = [x for x in nums[:i-1:-1]]
                return
        nums[:] = nums[::-1]

if __name__ == "__main__":
    test = Solution()
    case = [1,2,3]
    test.nextPermutation(case)
    print(case)
    case = [1,3,2]
    test.nextPermutation(case)
    print(case)
    case = [3,2,1]
    test.nextPermutation(case)
    print(case)
    case = [2,3,1]
    test.nextPermutation(case)
    print(case)
    case = [4,3,2,1]
    test.nextPermutation(case)
    print(case)
    case = []
    test.nextPermutation(case)
    print(case)
    case = [1,4,3,2]
    test.nextPermutation(case)
    print(case)