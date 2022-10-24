from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        cum_min = [0]*n
        cum_max = [0]*n
        for i in range(n):
            if i == 0:
                cum_max[i] = nums[i]
            else:
                cum_max[i] = max(cum_max[i-1], nums[i])
        for i in range(n-1, -1, -1):
            if i == n-1:
                cum_min[i] = nums[i]
            else:
                cum_min[i] = min(cum_min[i+1], nums[i])
        for i in range(n-1):
            if cum_max[i] <= cum_min[i+1]:
                break
        return i+1

if __name__ == '__main__':
    test = Solution()
    print(test.partitionDisjoint([5,0,3,8,6]))
    print(test.partitionDisjoint([1,1,1,0,6,12]))