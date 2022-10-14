from typing import List


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


if __name__ == '__main__':
    test = Solution()
    # print(test.maxChunksToSorted([4,3,2,1,0]))
    # print(test.maxChunksToSorted([1,0,2,3,4]))
    # print(test.maxChunksToSorted([0,1,2,3,4]))
    # print(test.maxChunksToSorted([1,2,0,3]))
    # print(test.maxChunksToSorted([1,4,2,0,3]))
    print(test.maxChunksToSorted([1,4,3,6,0,7,8,2,5]))