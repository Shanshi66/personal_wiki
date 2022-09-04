from asyncio import constants
from distutils.command.build import build
from math import inf
from typing import List

class Node():
    def __init__(self):
        self.l = 0
        self.r = 0
        self.sum_val = 0
        self.max_val = 0




class Solution:

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
            self.tree[cur].sum_val = max(self.tree[cur*2].sum_val, self.tree[cur*2+1].sum_val)

    def tree_find(self, cur, l, r):
        if self.tree[cur].l == l and self.tree[cur].r == r:
            return (self.tree[cur].max_val, self.tree[cur].sum_val)
        mid = (l+r) >> 1
        if r < mid:
            return self.tree_find(cur*2, l, r)
        elif l > mid:
            return self.tree_find(cur*2+1, l, r)
        else:
            max_val_l, sum_val_l = self.tree_find(cur*2, l, mid)
            max_val_r, sum_val_r = self.tree_find(cur*2+1, mid+1, r)
            return max(max_val_l, max_val_r), sum_val_l+sum_val_r
    
    def compute_cost(self, num, n):
        cost = inf
        for i in range(0, n, num):
            max_val, sum_val = self.tree_find(1, i, i+num)
            cost = min(max_val+num*sum_val, cost)
        return cost        

    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        self.tree = [Node() for i in range(4*n)]
        self.seg_tree = self.build_tree(chargeTimes, runningCosts, 1, 0, n-1)
        l, r = 0, n
        while l <= r:
            mid = (l+r) >> 1
            cost = self.compute_cost(mid, n)
            if cost > budget:
                r = mid-1
            else:
                l = mid+1
        return l

if __name__ == '__main__':
    test = Solution()
    print(test.maximumRobots([3,6,1,3,4], [2,1,3,4,5], 25))
