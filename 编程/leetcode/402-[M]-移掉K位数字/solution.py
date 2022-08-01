
# 思路：贪心，如果num[i] > num[i+1]，去掉num[i]会使结果变小，重复这么做。当遍历完一遍之后，剩余的序列中任意i，都有num[i] <= num[i+1]，当K还大于1时，截掉最后面的K位就行。
# 在num前后分别加上0，不影响结果，代码更简洁。

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k: # 剪枝
            return "0"
        num = '0'+num+'0'
        stack = []
        for c in num:
            while k > 0 and stack and c < stack[-1]: 
                stack.pop()
                k -= 1
            stack.append(c)
        return "".join(stack[1:-1]).lstrip("0") or "0"


if __name__ == '__main__':
    test = Solution()
    print(test.removeKdigits("1432219", 3))
    print(test.removeKdigits("1432319", 3))
    print(test.removeKdigits("1223", 1))
    print(test.removeKdigits("1223", 2))
    print(test.removeKdigits("10200", 1))
    print(test.removeKdigits("10", 2))
    print(test.removeKdigits("10", 3))
    print(test.removeKdigits("9", 3))
