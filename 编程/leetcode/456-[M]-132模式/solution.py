from typing import List

# 思路：遍历数组，维护一个单调递增队列，最大的元素表示中间值。有三种情况：
# 1. 如果中间值右边最大值比左边最小值还小，或者左边最小值比中间值还大，说明满足要求的三元组还没出现，需要重置队列。对于
# 2. 如果左边最小值比右边最大值或当前值小，并且比中间值小，满足要求
# 3. 如果以上都不满足，说明中间值还在后面，继续遍历

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        max_n = [x for x in nums]
        min_n = [x for x in nums]
        for i in range(1, n):
            min_n[i] = min(min_n[i-1], nums[i])
            max_n[n-i-1] = max(max_n[n-i], nums[n-i-1])
        stack = [(nums[1], 1)]
        for i in range(2, n):
            top_num = stack[-1][0]
            top_idx = stack[-1][1]
            if max_n[top_idx+1] <= min_n[top_idx-1] or min_n[top_idx-1] >= top_num:
                stack = [(nums[i], i)]
                continue
            if min_n[top_idx-1] < max_n[top_idx+1] < top_num or min_n[top_idx-1] < nums[i] < top_num:
                return True
            if nums[i] >= top_num:
                stack.append((nums[i], i))
        return False

if __name__ == '__main__':
    test = Solution()
    # print(test.find132pattern([1,2,3,4]))
    # print(test.find132pattern([-1,3,2,0]))
    # print(test.find132pattern([3,1,4,2]))
    # print(test.find132pattern([1,3,0,2]))
    # print(test.find132pattern([1,3,0,0]))
    # print(test.find132pattern([1,3,0,4,5,4]))
    # print(test.find132pattern([1,0,1,-4,-3]))
    # print(test.find132pattern([1,3,2,4,5,6,7,8,9,10]))
    print(test.find132pattern([40,50,25,35,15,35,20]))

