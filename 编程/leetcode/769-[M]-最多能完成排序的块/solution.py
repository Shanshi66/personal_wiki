from typing import List

# 思路：因为只有0 -> n-1这n个数，可以从最大数开始遍历起截取块，最大数到数组末尾一定属于一个块。如果当前数的index在已取得块之外，小于后面的最小值，则可以形成新的块。

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        num_idx = {}
        n = len(arr)
        if n == 1:
            return 1
        for idx, num in enumerate(arr):
            num_idx[num] = idx
        min_num = [n]*n
        for i in range(n-1, -1, -1):
            if i == n-1:
                min_num[i] = arr[i]
            else:
                min_num[i] = min(arr[i], min_num[i+1])
        i = n
        cnt = 0
        for num in range(n-1, -1, -1):
            idx = num_idx[num]
            if i == n or (idx < i and num < min_num[i]):
                cnt += 1
            i = min(i, idx)
        return cnt

# 官方思路：
# 因为数的范围是0 -> n-1, 排序好之后数i一定在i位置。因此可以遍历数组，如果max(a[0]..a[i]) == i, 则可以形成一个块。
# 问题：会不会存在最小值在很后面的情况？如果一个比较小的值在很后面，那么必定会交换到一个更大的值，当前最大值一定大于i。

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = mx = 0
        for i, x in enumerate(arr):
            mx = max(mx, x)
            ans += mx == i
        return ans

if __name__ == '__main__':
    test = Solution()
    # print(test.maxChunksToSorted([4,3,2,1,0]))
    # print(test.maxChunksToSorted([1,0,2,3,4]))
    # print(test.maxChunksToSorted([0,1,2,3,4]))
    # print(test.maxChunksToSorted([1,2,0,3]))
    # print(test.maxChunksToSorted([1,4,2,0,3]))
    print(test.maxChunksToSorted([1,4,3,6,0,7,8,2,5]))