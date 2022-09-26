from typing import List

# 思路：数组长度一定大于等于n-2，使用数组索引进行标识，对于n+1，n+2的缺失需要单独判断。这里的n是题目中的n，不是数组长度。

class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out_num = []

        for num in nums:
            num = abs(num)
            if num > n:
                out_num.append(num)
                continue
            if num <= n and nums[num-1] > 0:
                nums[num-1] = -nums[num-1]
        
        res = []
        for i in range(n):
            if nums[i] > 0 and len(res) < 2:
                res.append(i+1)
        
        if len(res) == 0: # 数组长度n-2，最大的两个数缺失
            res.append(n+1)
            res.append(n+2)
        elif len(res) == 1: # 数组长度n-1或n-2
            if not out_num:
                res.append(n+1)
            elif out_num[0] > n+1: # n存在，缺失的是n-1
                res.append(n+1)
            else:
                res.append(n+2)
        return res
        

if __name__ == '__main__':
    test = Solution()
    print(test.missingTwo([1]))
    print(test.missingTwo([2,3]))
    print(test.missingTwo([2,3,2]))
    print(test.missingTwo([2,3,2,4,2]))
    print(test.missingTwo([]))
            
            