from cmath import inf
from typing import List


# 思路：先排序，保证以i为起点的数对链是在i的左侧，dp[i]表示以i为起点的数对链最长长度。

class Solution1:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1], reverse = True)
        dp = [1]*len(pairs)
        for i in range(1, len(pairs)):
            for j in range(i):
                if pairs[j][0] > pairs[i][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


# 思路：贪心，每次选择右边界最小的pair

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        right, ans = -inf, 0
        for x, y in pairs:
            if right < x:
                right = y
                ans += 1
        return ans


# 其他思路：arr[i]表示长度为i+1的数链对的最小右边界值

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        arr = []
        for x, y in pairs:
            i = bisect_left(arr, x)
            if i < len(arr):
                arr[i] = min(arr[i], y)
            else:
                arr.append(y)
        return len(arr)

if __name__ == "__main__":
    test = Solution()
    print(test.findLongestChain([[1,2], [2,3], [3,4]]))
    print(test.findLongestChain([[5,6], [2,7], [3,4], [1,2]]))