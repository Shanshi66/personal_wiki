from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        dp = [1]*n
        for i in range(n-2, -1, -1):
            for j in range(i+1, i+1+dp[i+1]):
                if nums[i]&nums[j] != 0:
                    break
            else:
                j += 1
            dp[i] = j-i
        return max(dp)


if __name__ == '__main__':
    test = Solution()
    print(test.longestNiceSubarray([1,3,8,48,10]))
    print(test.longestNiceSubarray([3,1,5,11,13]))
            