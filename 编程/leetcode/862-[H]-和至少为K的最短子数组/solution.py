from collections import deque
from typing import List


# 思路：利用前缀和来求解区间的和，有两个优化点
# 1. 对于左边界i，如果第一次出现右边界j，i->j区间的和大于K，那么对于左边界i来说，j是最优值，可以不用考虑了
# 2. 对于一个右边界，最优解只需要考虑最右最小的左边界(前缀和)即可

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = n+1
        acc_sum = [0]
        for i in range(n):
            acc_sum.append(acc_sum[i]+nums[i])
        que = deque()
        for i, acc in enumerate(acc_sum):
            while que and acc-acc_sum[que[0]] >= k:
                res = min(res, i-que.popleft()) # 优化1
            while que and acc < acc_sum[que[-1]]:
                que.pop() # 优化2
            que.append(i)
        return res if res < n+1 else -1
        
if __name__ == '__main__':
    test = Solution()
    # print(test.shortestSubarray([1], k=1))
    # print(test.shortestSubarray([1,2], k=4))
    # print(test.shortestSubarray([2,-1,2], k=3))
    # print(test.shortestSubarray([5,1,6,2,4,3], k=10))
    # print(test.shortestSubarray([5,1,6,2,4,3], k=9))
    # print(test.shortestSubarray([5,1,6,2,4,3], k=8))
    # print(test.shortestSubarray([5,1,6,2,4,3], k=11))
    # print(test.shortestSubarray([84,-37,32,40,95], k=167))
    print(test.shortestSubarray([-34,37,51,3,-12,-50,51,100,-47,99,34,14,-13,89,31,-14,-44,23,-38,6]
, 151))