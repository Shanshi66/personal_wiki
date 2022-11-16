from typing import List

# 思路：局部倒置很好求，全局倒置通过归并排序求逆序对

class Solution:
    def merge_sort(self, nums, left, right):
        if right-left <= 1:
            return 0
        mid = (left+right)//2
        res_left = self.merge_sort(nums, left, mid)
        res_right = self.merge_sort(nums, mid, right)
        new_nums = []
        i, j = left, mid
        res = 0
        while i < mid and j < right:
            if nums[i] <= nums[j]:
                new_nums.append(nums[i])
                i += 1
            else:
                new_nums.append(nums[j])
                res += mid-i # nums[j]能产生mid-1个逆序对
                j += 1
        while i < mid: 
            new_nums.append(nums[i])
            i += 1
        while j < right:
            new_nums.append(nums[j])
            j += 1
        nums[left:right] = new_nums
        return res+res_left+res_right

    def isIdealPermutation(self, nums: List[int]) -> bool:
        target = 0
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                target += 1
        res = self.merge_sort(nums, 0, n)
        if target == res:
            return True
        return False

# 官方思路1：
# 1. 局部倒置一定是全局倒置，问题转转变为是否存在局部倒置之外的全局倒置。
# 2. 维护后缀最小值，对于元素num[i]，判断num[i] > min(num[i+2], num[i+3]...)即可

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        min_suf = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            if nums[i - 1] > min_suf: # min_suf是min(nums[i+1],num[i+2]...)
                return False
            min_suf = min(min_suf, nums[i])
        return True

# 官方思路2：
# 1. 局部倒置一定是全局倒置，因此不能存在非局部倒置的全局倒置，即不能存在j>i+1，nums[j] < nums[i]
# 2. 对于最小值0，其下标不能超过2
# 3. 倒置只会增加不会减少
# 因此：
# 1. 如果nums[0] == 0, 问题转化为子问题：判断nums[1:n]是否为理想排列
# 2. 如果nums[1] == 0, 那么nums[0] == 1，问题转化为子问题：判断nums[2:n]是否为理想队列
# 可归纳出：
# |nums[i]-i|<=1

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        return all(abs(x - i) <= 1 for i, x in enumerate(nums))


if __name__ == '__main__':
    test = Solution()
    print(test.isIdealPermutation([1,0,2]))
    print(test.isIdealPermutation([1,2,0]))
    print(test.isIdealPermutation([1]))