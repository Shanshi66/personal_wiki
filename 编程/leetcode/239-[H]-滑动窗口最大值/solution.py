import heapq
from heapq import heappop, heappush, heapify
from typing import List

# 思路：大顶堆，不删除元素，如果最大元素过期再删除。O(nlogn)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return [max(nums)]
        num_freq = {}
        heap = [-x for x in nums[0:k]]
        heapify(heap)
        for n in heap:
            num_freq.setdefault(n, 0)
            num_freq[n] += 1
        result = []
        for i in range(k, len(nums)+1):
            while True:
                max_item = heap[0]
                if not num_freq[max_item]:
                    heappop(heap)
                    continue
                result.append(-max_item)
                break
            if i == len(nums):
                break
            start = nums[i-k]
            num_freq[-start] -= 1
            heappush(heap, -nums[i])
            num_freq.setdefault(-nums[i], 0)
            num_freq[-nums[i]] += 1
        return result


# 优化：使用下标进行过期判断
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans

# 思路二：单调队列，对于一个滑动窗口，维护一个单调递减队列，对于窗口中i < j, num[i] < num[j]的元素, num[i]会被删除，第一个元素就是最大的。O(n)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])
        
        return ans


# 思路三：有趣的思路，将数组分为k组，在每个分组内维护premax, postmax两个数组，premax[i]表示i对应的分组中，以i为结尾的最大值，postmax[i]表示i对应的分组中，以i为开始的最大值。
# 以i开始的区间，要么和一个分组重合，要么跨了分组。结果都是：
# max{premax[i+k-1], postmax[i]}
# O(n)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefixMax, suffixMax = [0] * n, [0] * n
        for i in range(n):
            if i % k == 0:
                prefixMax[i] = nums[i]
            else:
                prefixMax[i] = max(prefixMax[i - 1], nums[i])
        for i in range(n - 1, -1, -1):
            if i == n - 1 or (i + 1) % k == 0:
                suffixMax[i] = nums[i]
            else:
                suffixMax[i] = max(suffixMax[i + 1], nums[i])

        ans = [max(suffixMax[i], prefixMax[i + k - 1]) for i in range(n - k + 1)]
        return ans

if __name__ == '__main__':
    test = Solution()
    print(test.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    print(test.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 5))
    print(test.maxSlidingWindow([3,5], 5))


