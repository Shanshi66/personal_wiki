from typing import List

# 枚举两个数， 看剩下的差是否能找到
# 对数组排序，记录下同一个数最右边的idx，保证不重复

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        ans_set = set()
        num_dict = {}
        nums.sort()
        for idx, num_ in enumerate(nums):
            num_dict[num_] = idx
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                target = -(nums[i]+nums[j])
                if target < nums[j]: # 保证不重复
                    break
                if target in num_dict and num_dict[target] > j:
                    ans_set.add((nums[i], nums[j], target))
        return list(ans_set)


if __name__ == "__main__":
    test = Solution()
    print(test.threeSum([-1,0,1,2,-1,-4]))
    print(test.threeSum([]))
    print(test.threeSum([0]))
    print(test.threeSum([0,0]))
    print(test.threeSum([0,0,0]))
    print(test.threeSum([1,0,-1]))
    print(test.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))