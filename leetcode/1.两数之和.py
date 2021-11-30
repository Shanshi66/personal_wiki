#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        for idx, num in enumerate(nums):
            num_index.setdefault(num, idx)
        res = None
        for num in num_index:
            if not target-num in num_index:
                continue
            res = [num_index[num], num_index[target-num]]
        return res

# @lc code=end

