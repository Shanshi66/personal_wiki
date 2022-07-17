import bisect
from os import stat
from typing import List

# 思路：<超时> 遍历每个柱子，看以这个柱子为右边界的矩形最大面积。<陷入单调栈的陷阱，强行用，没有从最基础的优化角度出发>

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        index = []
        stack = []
        max_result = 0
        for i in range(len(heights)):
            max_result = max(max_result, heights[i])
            if i == 0:
                stack.append(heights[i])
                index.append(i)
                continue
            if heights[i] >= stack[-1]:
                for h, idx in zip(stack, index):
                    max_result = max(max_result, h*(i-idx+1))
                if heights[i] > stack[-1]:
                    stack.append(heights[i])
                    index.append(i)
            else:
                for j in range(0, len(stack)):
                    if stack[j] < heights[i]:
                        max_result = max(max_result, stack[j]*(i-index[j]+1))
                    else:
                        max_result = max(max_result, heights[i]*(i-index[j]+1))
                        stack[j] = heights[i]
                        stack = stack[0:j+1]
                        index = index[0:j+1]
                        break
        return max_result

# 思路：枚举矩形高度，找出符合该高度的左右边界。使用单调栈，栈中的高度依次递增，对于第i个柱子，如果栈顶柱子高度大于i，将其弹出栈，直到找到第一个高度小于i的柱子。为什么弹出栈可以？因为如果对于i后面的柱子来说，高于i的柱子左边界不可能比i小。
# 右边界可以使用同样的方法找到，但可以更简单。对于栈中的一个柱子，如果被弹出，意味着右边第一个小于该柱子的柱子找到了。（如果有相同的柱子的情况，假设5个，这种方法前4个右边界会有问题，但是第五个正确，对结果没有影响）

class Solution1:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        left = [-1]*n
        right = [n]*n
        max_area = 0
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                right[stack[-1]] = i
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        for i in range(n):
            max_area = max(max_area, (right[i]-left[i]-1)*heights[i])
        return max_area



if __name__ == "__main__":
    test = Solution1()
    print(test.largestRectangleArea([2,1,5,6,2,3]))
    print(test.largestRectangleArea([2,4]))
    print(test.largestRectangleArea([2,1,5,6,3,3]))
    print(test.largestRectangleArea([2]))
    print(test.largestRectangleArea([5,4,1,2]))
    print(test.largestRectangleArea([3,1,4,5,3,2,7,5,3]))
    print(test.largestRectangleArea([]))
                    
            
                    
