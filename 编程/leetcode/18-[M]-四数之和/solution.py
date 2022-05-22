from typing import List, Tuple, Dict

from sklearn import tree

# 枚举第三个数，遍历左边两个数，看第四个数在不在数组里

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        num_dict = {}
        for i, n in enumerate(nums):
            num_dict[n] = i
        ans_set = set()
        for i in range(2, len(nums)):
            for j in range(0, i):
                for k in range(j+1, i):
                    left = target-(nums[i]+nums[j]+nums[k])
                    if left < nums[i]:
                        break
                    if left in num_dict and num_dict[left] > i:
                        ans_set.add((nums[j], nums[k], nums[i], left))
        ans_set = [list(x) for x in ans_set]
        return ans_set

if __name__ == "__main__":
    test = Solution()
    print(test.fourSum([1,0,-1,0,-2,2], 0))
    print(test.fourSum([1,0,-1,0,-2,2], 1))
    print(test.fourSum([2,2,2,2,2,2], 8))
    print(test.fourSum([2,2,2], 8))
    print(test.fourSum([2,2,2,2], 9))
