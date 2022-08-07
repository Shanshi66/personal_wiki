from typing import List

# 思路：单调栈+哈希表，从前往后遍历，维护一个单调减栈，每次弹出一个元素，必然是遇到了该元素第一个比它大的元素

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_bigger = {}
        stack = []
        for num in nums2:
            if not stack or num <= stack[-1]:
                stack.append(num)
                continue
            while stack and num > stack[-1]:
                next_bigger[stack[-1]] = num
                stack.pop()
            stack.append(num)
        ans = []
        for num in nums1:
            if num in next_bigger:
                ans.append(next_bigger[num])
            else:
                ans.append(-1)
        return ans


if __name__ == '__main__':
    test = Solution()
    print(test.nextGreaterElement([4,1,2], [1,3,4,2]))
    print(test.nextGreaterElement([2,4], [1,2,3,4]))
    print(test.nextGreaterElement([10,5,1,2], [1,10,5,7,2,3,4]))
        