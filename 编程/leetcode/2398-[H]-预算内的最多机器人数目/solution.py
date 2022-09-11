from asyncio import constants
from distutils.command.build import build
from math import inf
from typing import List
from collections import deque
class Node():
    def __init__(self):
        self.l = 0
        self.r = 0
        self.sum_val = 0
        self.max_val = 0

# 思路：二分区间长度，针对每个区间长度，枚举每个区间，时间复杂度:O(n*logn*logn),超时。
class Solution1:
    def build_tree(self, chargeTime, runningCost, cur, l, r):
        self.tree[cur].l, self.tree[cur].r = l, r
        if l == r:
            self.tree[cur].sum_val = runningCost[l]
            self.tree[cur].max_val = chargeTime[l]
        if l < r:
            mid = (l+r) >> 1
            self.build_tree(chargeTime, runningCost, cur*2, l, mid)
            self.build_tree(chargeTime, runningCost, cur*2+1, mid+1, r)
            self.tree[cur].max_val = max(self.tree[cur*2].max_val, self.tree[cur*2+1].max_val)
            self.tree[cur].sum_val = self.tree[cur*2].sum_val+self.tree[cur*2+1].sum_val

    def tree_find(self, cur, l, r):
        if self.tree[cur].l == l and self.tree[cur].r == r:
            return (self.tree[cur].max_val, self.tree[cur].sum_val)
        mid = (self.tree[cur].l+self.tree[cur].r)//2
        if r <= mid:
            return self.tree_find(cur*2, l, r)
        elif l > mid:
            return self.tree_find(cur*2+1, l, r)
        else:
            max_val_l, sum_val_l = self.tree_find(cur*2, l, mid)
            max_val_r, sum_val_r = self.tree_find(cur*2+1, mid+1, r)
            return max(max_val_l, max_val_r), sum_val_l+sum_val_r
    
    def compute_cost(self, num, n, budget):
        cost = inf
        for i in range(0, n-num+1):
            max_val, sum_val = self.tree_find(1, i, i+num-1)
            cost = min(max_val+num*sum_val, cost)
            # print(i, i+num-1, cost)
            if cost < budget:
                return cost
        return cost

    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        self.tree = [Node() for _ in range(4*n+1)]
        self.seg_tree = self.build_tree(chargeTimes, runningCosts, 1, 0, n-1)
        l, r = 0, n
        while l <= r:
            mid = (l+r) >> 1
            if mid == 0:
                break
            cost = self.compute_cost(mid, n, budget)
            if cost > budget:
                r = mid-1
            else:
                l = mid+1
        return r


# 思路：单调队列+双指针，参考239，维护单调递减队列，区间最大值为第一个元素。不断追加元素，如果超budget，区间左边+1。

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        running_cost_arr = [0]*n
        for i in range(n):
            running_cost_arr[i] = runningCosts[i] if i == 0 else runningCosts[i]+running_cost_arr[i-1]
        que = deque()
        result = 0
        i = 0
        for j in range(n):
            while que and chargeTimes[j] > chargeTimes[que[-1]]:
                que.pop()
            que.append(j)
            while que:
                if j != i:
                    cost = chargeTimes[que[0]]+(j-i+1)*(running_cost_arr[j]-running_cost_arr[i]+runningCosts[i])
                else:
                    cost = chargeTimes[que[0]]+runningCosts[i]
                if cost <= budget:
                    result = max(result, j-i+1)
                    break
                else:
                    if i == que[0]:  # 注意，如果左区间索引跟队列第一个重合，+1的同时要pop掉。
                        que.popleft()
                    i += 1 
        return result


if __name__ == '__main__':
    test = Solution()
    print(test.maximumRobots([3,6,1,3,4], [2,1,3,4,5], 25))
    print(test.maximumRobots([11,12,19], [10,8,7], 19))
    print(test.maximumRobots([11,12,19], [10,8,7], 50))
    print(test.maximumRobots([11,12,74,67,37,87,42,34,18,90,36,28,34,20],[18,98,2,84,7,57,54,65,59,91,7,23,94,20], 937))
    print(test.maximumRobots([54,30,92,63,31],[28,99,86,19,5],85))
    # print(test.maximumRobots([19,63,21,8,5,46,56,45,54,30,92,63,31,71,87,94,67,8,19,89,79,25],[91,92,39,89,62,81,33,99,28,99,86,19,5,6,19,94,65,86,17,10,8,42],85))
    # print(test.maximumRobots([63,31],[19,5], 85))
