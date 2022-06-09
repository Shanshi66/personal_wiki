from typing import List

# 将数字n放到index=n-1的位置，遍历数组查看第一个有空缺的位置

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            while nums[i] <= len(nums) and nums[i] > 0 and nums[i]-1 != i and nums[i] != nums[nums[i]-1]:
                tmp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = tmp
        for i in range(0, len(nums)):
            if nums[i]-1 != i:
                break
        else:
            i = i+1
        return i+1

if __name__ == '__main__':
    test = Solution()
    print(test.firstMissingPositive([1,2,0]))
    print(test.firstMissingPositive([3,4,-1,1]))
    print(test.firstMissingPositive([7,8,9]))
    print(test.firstMissingPositive([0]))
    print(test.firstMissingPositive([0,1,1,2]))
    print(test.firstMissingPositive([0,1,1,3]))
    print(test.firstMissingPositive([0,1,2,3]))
    print(test.firstMissingPositive([-1,-2,1,2,3]))
    print(test.firstMissingPositive([1]))
        