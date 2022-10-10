from typing import List


# 思路：对于位置i是否交换，只和i-1有关，可用动态规划求解。dp[i][0]表示第i个位置不交换使得前i个数字满足条件的最小次数，dp[i][1]表示第i个位置交换使得前i个数字满足条件的最小次数。

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [[n+1]*2 for _ in range(n)]
        dp[0][0], dp[0][1] = 0, 1
        for i in range(1, n):
            if dp[i-1][0] < n+1 and nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                dp[i][0] = min(dp[i][0], dp[i-1][0])
            if dp[i-1][1] < n+1 and nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                dp[i][0] = min(dp[i][0], dp[i-1][1])
            if dp[i-1][0] < n+1 and nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                dp[i][1] = min(dp[i][1], dp[i-1][0]+1)
            if dp[i-1][1] < n+1 and nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                dp[i][1] = min(dp[i][1], dp[i-1][1]+1)
        
        res = min(dp[n-1][0], dp[n-1][1])
        return res


if __name__ == '__main__':
    test = Solution()
    print(test.minSwap([1,3,5,4], [1,2,3,7]))
    print(test.minSwap([0,3,5,8,9], [2,1,4,6,9]))
    print(test.minSwap([1,3,5,4], [1,2,3,7]))
    print(test.minSwap([1,2,3,4], [1,2,3,4]))
    print(test.minSwap([1,5,10,20], [2,7,6,8]))
    print(test.minSwap([1,5,10,20,30], [0,7,6,22,21]))
        