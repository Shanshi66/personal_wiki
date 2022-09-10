from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sum_set = set()
        for i in range(len(nums)-1):
            tmp = nums[i]+nums[i+1]
            if tmp in sum_set:
                return True
            sum_set.add(tmp)
        return False



if __name__ == "__main__":
    test = Solution()
    print(test.findSubarrays([0,0,0]))
        