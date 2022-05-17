from typing import List

# 双指针：对于边界s、t，假设s是短边，那么t不管怎么往左移，都不会比当前情况大，所以s+1缩小子问题。(t往右移的情况已经考虑过了)
# 剪枝: 对于边界s、t，最优解是(t-s)*maxh，如果当前答案比这个还大，没必要往下搜索了

class Solution:
    def maxArea(self, height: List[int]) -> int:
        s_idx = 0
        e_idx = len(height)-1
        max_area = -1
        max_h = max(height)
        while s_idx < e_idx:
            max_area = max(max_area, (e_idx-s_idx)*min(height[s_idx], height[e_idx]))
            if height[s_idx] > height[e_idx]:
                e_idx -= 1
            else:
                s_idx += 1
            if max_area >= max_h*(e_idx-s_idx): # 剪枝
                break
        return max_area


if __name__ == '__main__':
    test = Solution()
    print(test.maxArea([1,1]))
    print(test.maxArea([1,8,6,2,5,4,8,3,7]))