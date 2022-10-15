# 思路：
# 观察到，结尾相同的子串只需要保留最后一次出现位置的结果即可,比如，abcb, 第一个b为结尾的子串，b和ab，完全可以由最后一个b实现。因此可以有以下动态转移方式。
# dp[i]表示以第i个字符结尾的子串数量，dp[i] = 1+dp[last['a']]+dp[last['b']]+... = 1+sum(dp[last[char]]]])1表示长度为1的字符串
# sum部分可以滚动求和，减掉重复的部分即可。

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = int(1e9+7)
        total = 0
        last = [0]*26
        for c in s:
            idx = ord(c)-ord('a')
            pre = last[idx]
            last[idx] = (1+total)%mod
            total += last[idx]-pre
            total = total%mod
        return total


if __name__ == '__main__':
    test = Solution()
    print(test.distinctSubseqII("abc"))
    print(test.distinctSubseqII("aba"))
    print(test.distinctSubseqII("aaa"))