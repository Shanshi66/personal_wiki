
# 思路：零的个数等于2*5 pair的个数，由于5的数量肯定比2少(5>2*2，在增加一个5之前，至少加了2个2)，只需要考虑5的个数即可。

class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        for num in range(5, n+1, 5):
            i = num
            while i > 0 and i%5 == 0:
                res += 1
                i = i//5
        return res


# 思路：[1, n]中p的倍数有floor(n/p)个，这些数至少贡献1个p因子。p^2的倍数有floor(n/p/p)个，这些数额外贡献一个p因子，依次类推。总共包含sum(floor(n/p^i))个p因子,i=1...k。


class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n >= 5:
            n //= 5
            ans += n
        return ans

if __name__ == '__main__':
    test = Solution()
    print(test.trailingZeroes(0))
    print(test.trailingZeroes(5))
    print(test.trailingZeroes(10))
    print(test.trailingZeroes(15))
    print(test.trailingZeroes(20))
    print(test.trailingZeroes(100))
