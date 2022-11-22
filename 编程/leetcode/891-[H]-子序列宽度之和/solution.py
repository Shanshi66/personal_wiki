from typing import List

# 思路：排序，枚举两个端点作为最小值和最大值，中间的数任取可以满足序列要求。
# 长度为2的序列和是：(a1-a0)*c(0,0) + (a2-a1)*c(0,0)+...+(an-a_{n-1})*c(0,0)
# 长度为3的序列和是：(a2-a0)*[c(1,0)+c(1,1)] + (a3-a1)*[c(1,0)+c(1,1)]+...+(an-a_{n-2})*[c(1,0)+c(1,1)]
# 以此类推，长度为k+2的序列结果 = (sum(n -> n-k) - sum(0 -> k)) * (c(k,0)+c(k, 1)+c(k, 2)+ ... + c(k,k))
# (c(k,0)+c(k, 1)+c(k, 2)+ ... + c(k,k)) = 2^n

class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        e = 0
        i, j = 0, len(nums)-1
        sum_pre = 0
        sum_post = 0        
        nums.sort()
        res = 0
        mod = int(1e9+7)
        exp = [1]*int(1e5+5)
        for i in range(1, int(1e5+5)):
            exp[i] = (exp[i-1]*2)%mod
        i = 0
        while i < len(nums):
            sum_pre += nums[i]
            sum_post += nums[j]
            res += (((sum_post-sum_pre)%mod)*exp[e])%mod
            res = res%mod
            e += 1
            i += 1
            j -= 1
        return res


if __name__ == '__main__':
    test = Solution()
    print(test.sumSubseqWidths([2,1,3]))
    print(test.sumSubseqWidths([2]))