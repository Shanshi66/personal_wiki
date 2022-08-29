
# 思路：参考172。总共包含sum(floor(n/p^i))个p因子,i=1...k，枚举每一个floor(n/p)，求出sum，判断是否可以得到k。因为k与sum()之间是单调递增的关系，可以二分。
# 结果只会是0或5，如果存在f(x)=k，在下一个因子5出现之前f(x)都等于k，而每5个数出现一个因子5.

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        left = 0
        right = k
        while left <= right:
            mid = (right-left)//2+left
            ans = mid
            tmp = mid
            while tmp >= 5:
                tmp = tmp//5
                ans += tmp
            if ans > k:
                right = mid-1
            elif ans == k:
                return 5
            else:
                left = mid+1
        return 0

if __name__ == '__main__':
    test = Solution()
    print(test.preimageSizeFZF(100))
    print(test.preimageSizeFZF(0))
    print(test.preimageSizeFZF(5))
    print(test.preimageSizeFZF(3))