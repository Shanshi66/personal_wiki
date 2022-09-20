from functools import cache, lru_cache
from typing import List

# 思路：状态压缩+搜索，因为数组长度只有16，可以用16位整数进行标识。
# cache与lru_cache的区别，cache是不做size限制的lru_cache
# 时间复杂度: O(n*2^n)，2^n个状态，每个状态遍历一次

class Solution1:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        n = len(nums)
        max_num = max(nums)
        if total%k > 0:
            return False
        per_sum = total//k
        if max_num > per_sum:
            return False
        nums.sort()

        @cache
        def dfs(s, p):
            if s == 0:
                return True
            for i in range(n):
                if p+nums[i] > per_sum:
                    break
                if (s>>i)&1 and dfs(s^(1<<i), (p+nums[i])%per_sum):
                    return True
            return False
        return dfs((1<<n)-1, 0)

# 思路：动态规划+状态压缩。遍历每个状态，如果可以进行下一次选择，标记为true。当只剩下一个数时，如果还可以选择下一个数，那一定就是可行的答案

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        n = len(nums)
        max_num = max(nums)
        if total%k > 0:
            return False
        per_sum = total//k
        if max_num > per_sum:
            return False
        nums.sort()
        dp = [False]*(1<<n)
        dp[0] = True
        statu_sum = [0]*(1<<n)
        for i in range(1<<n):
            if not dp[i]:
                continue
            for j in range(n):
                if (i>>j)&1:
                    continue
                if statu_sum[i]+nums[j] > per_sum:
                    break
                dp[i|(1<<j)] = True
                statu_sum[i|1<<j] = (statu_sum[i]+nums[j])%per_sum
        return dp[(1<<n)-1]




if __name__ == '__main__':
    test = Solution()
    print(test.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
    print(test.canPartitionKSubsets([1,2,3,4], 3))
    print(test.canPartitionKSubsets([815,625,3889,4471,60,494,944,1118,4623,497,771,679,1240,202,601,883], 3))
        
