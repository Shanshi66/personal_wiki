from collections import deque
import heapq


# 方法一：最小堆，每次从堆顶取一个元素乘上3、5、7，第k堆顶的元素就是第k个数

class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        heap = [1]
        nums = set([1])
        for i in range(k-1):
            top = heapq.heappop(heap)
            if top*3 not in nums:
                nums.add(top*3)
                heapq.heappush(heap,top*3)
            if top*5 not in nums:
                nums.add(top*5)
                heapq.heappush(heap,top*5)
            if top*7 not in nums:
                nums.add(top*7)
                heapq.heappush(heap,top*7)

        return heap[0]

# 方法二：dp，维护3个指针p3,p4,p5分别指向上一次乘因子的位置dp[i] = min(dp[p3]*3, dp[p5]*5, dp[p7]*7)

class Solution1:
    def getKthMagicNumber(self, k: int) -> int:
        dp = [0]*k
        dp[0] = 1
        p3 = p5 = p7 = 0
        i = 1
        while i < k:
            dp[i] = min(dp[p3]*3, dp[p5]*5, dp[p7]*7)
            if dp[i] == dp[p3]*3:
                p3 += 1
            if dp[i] == dp[p5]*5:
                p5 += 1
            if dp[i] == dp[p7]*7:
                p7 += 1
            i += 1
        return dp[k-1]
                



if __name__ == '__main__':
    test = Solution()
    print(test.getKthMagicNumber(251))
