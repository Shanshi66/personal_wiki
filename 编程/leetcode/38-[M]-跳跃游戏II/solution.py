from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [len(nums)]*len(nums)
        dp[-1] = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i]+i >= len(nums)-1:
                dp[i] = 1
            else:
                for j in range(1, nums[i]+1):
                    dp[i] = min(dp[i], dp[i+j]+1)
        return dp[0]

if __name__ == '__main__':
    test = Solution()
    print(test.jump([2,3,1,1,4]))
    print(test.jump([2,3,0,1,4]))
    print(test.jump([4,1,1,1]))
    print(test.jump([1]))
    print(test.jump([1,1,1,1]))