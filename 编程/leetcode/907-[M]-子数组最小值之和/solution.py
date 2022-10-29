from turtle import left
from typing import List

# 思路：只要知道以arr[i]为最小元素的最长区间边界，就可以求出以arr[i]为最小元素的所有区间数量K，最终结果sum(K*arr[i]) for each i
# 用单调栈求区间，如果当前元素比栈顶元素小，一直弹出，直到左边界。如果当前元素被弹出，则到达右边界。

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left_margin = []
        stack = []
        res = 0
        mod = int(1e9+7)
        for i in range(n):
            idx = i
            while stack and arr[i] <= arr[stack[-1]]:
                idx = stack.pop()
                res += (idx-left_margin[idx]+1)*(i-idx)*arr[idx]
                res = res%mod
            if idx == i:
                left_margin.append(idx)
            else:
                left_margin.append(left_margin[idx])
            stack.append(i)
        while stack:
            idx = stack.pop()
            res += (idx-left_margin[idx]+1)*(n-idx)*arr[idx]
            res = res%mod
        return res

if __name__ == '__main__':
    test = Solution()
    print(test.sumSubarrayMins([3,1,2,4]))
    print(test.sumSubarrayMins([11,81,94,43,3]))
    print(test.sumSubarrayMins([3]))
    print(test.sumSubarrayMins([81,55,2]))