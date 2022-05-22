import math
from typing import Dict, List, Tuple

# 枚举gap，子问题为三数之和

class Solution:
    def threeSum(self, nums: List[int], num_dict: Dict[int, int], target: int) -> Tuple[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                left = target-(nums[i]+nums[j])
                if left < nums[j]:
                    break
                if left in num_dict and num_dict[left] > j:
                    return (nums[i], nums[j], left)
        return ()
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        num_dict = {}
        for idx, num_ in enumerate(nums):
            num_dict[num_] = idx
        max_sum = nums[-3]+nums[-2]+nums[-1]
        min_sum = nums[0]+nums[1]+nums[2]
        max_gap = max(abs(max_sum-target), abs(min_sum-target))
        for i in range(0, max_gap+1):
            res1 = self.threeSum(nums, num_dict, target-i)
            res2 = self.threeSum(nums, num_dict, target+i)
            if res1:
                ans = sum(res1)
                break
            if res2:
                ans = sum(res2)
                break
        return ans



if __name__ == "__main__":
    test = Solution()
    print(test.threeSumClosest([0,0,0], 1))