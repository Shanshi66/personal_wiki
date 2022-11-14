import functools


from functools import cache
from typing import List

# 思路：枚举其中一个数组的长度，因为有A_sum/B_sum = A_len / B_len，A_sum+B_sum = all_sum, A_len+B_len=n
# 可以求出其中一个数组的长度和，然后检查这种情况是否可能存在
# 超时

class Solution:
    @cache
    def check(self, part_sum, t, start):
        if part_sum == 0 and t == 0:
            return True
        if part_sum > 0 and t <= 0:
            return False
        if start == len(self.nums) or part_sum < 0 or t < 0:
            return False
        return (self.check(part_sum, t, start+1) | 
            self.check(part_sum-self.nums[start], t-1, start+1))

    def splitArraySameAverage(self, nums: List[int]) -> bool:
        self.nums = nums
        total_sum = sum(nums)
        n = len(nums)
        for l in range(1, n):
            r = n-l
            part_sum = total_sum/(l/r+1)
            if int(part_sum) != part_sum:
                continue
            if self.check(part_sum, r, 0):
                return True
        return False

# 思路：可以得到结论，子数组A的平均值等于整体数组的平均值，因此可以将所有数组元素减去均值，问题转化为求一个和为0的子数组。
# 将数组平均分成2部分，子数组要么存在左边或右边，要么左边为x，右边为-x，相加为0。
# 时间复杂度：O(2*2^{n/2})

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False

        s = sum(nums)
        for i in range(n):
            nums[i] = nums[i] * n - s # 乘n防止浮点数误差

        m = n // 2
        left = set()
        for i in range(1, 1 << m): # 用二进制表示状态
            tot = sum(x for j, x in enumerate(nums[:m]) if i >> j & 1)
            if tot == 0: # 数组和为0的子数组在左边
                return True
            left.add(tot)

        rsum = sum(nums[m:])
        for i in range(1, 1 << (n - m)):
            tot = sum(x for j, x in enumerate(nums[m:]) if i >> j & 1)
            if tot == 0 or rsum != tot and -tot in left:
                return True
        return False

# 思路：转化为背包问题，对于长度为k的子数组，均值为整体数组的均值avg，那么和为avg*k。那么问题转变成从长度为n的数组里选k个数，和为avg*k
# dp[i][x]表示长度为i，和为x的状态是否可能
# dp[i+1][x+nums[j]] = dp[i][x]

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        m = n // 2
        s = sum(nums)
        # 其中一个数组和为 sum_A = (total_sum*k)/n，必须是整数，且长度必定小于等于n/2
        if all(s * i % n for i in range(1, m + 1)): 
            return False

        dp = [set() for _ in range(m + 1)]
        dp[0].add(0)
        for num in nums:
            for i in range(m, 0, -1):
                for x in dp[i - 1]:
                    curr = x + num
                    if curr * n == s * i:
                        return True
                    dp[i].add(curr)
        return False


if __name__ == '__main__':
    test = Solution()
    # print(test.splitArraySameAverage([1,2,3,4,5,6,7,8]))
    # print(test.splitArraySameAverage([3,1]))
    # print(test.splitArraySameAverage([18,10,5,3]))
    print(test.splitArraySameAverage([0,0,0,0,0]))