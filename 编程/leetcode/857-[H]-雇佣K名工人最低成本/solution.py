from typing import List
import heapq
from math import inf

# 没想出来，看题解。思路：将quality理解成时间更好理解，枚举时薪ri = wage[i]/quality[i]，如果按ri发工资，时薪低于ri的均满足最低工资要求，这是选择最小的k个q即可
# 先按ri对数组排序，从前往后遍历，然后用堆维护一个大顶堆，选择最小的k个q即可，总工资未sumq*ri

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pair = sorted(zip(quality, wage), key = lambda x: x[1]/x[0])
        heap = []
        total_q = 0
        ans = inf
        for q, w in pair[:k-1]:
            total_q += q
            heapq.heappush(heap, -q)
        for q, w in pair[k-1:]:
            total_q += q
            heapq.heappush(heap, -q)
            ans = min(ans, total_q*w/q)
            total_q += heapq.heappop(heap)
        return ans


if __name__ == '__main__':
    test = Solution()
    print(test.mincostToHireWorkers([10,20,5], [70,50,30], 2))
    print(test.mincostToHireWorkers([3,1,10,10,1], [4,8,2,2,7], 3))