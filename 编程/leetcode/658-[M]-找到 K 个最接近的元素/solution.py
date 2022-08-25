import math
from typing import List
from bisect import bisect_left

# 思路：排序

class Solution1:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        new_arr = [num-x for num in arr]
        new_arr.sort(key = lambda x: (abs(x), x))
        result = [x+num for num in new_arr[0:k]]
        result.sort()
        return result

# 思路：二分查找。先找到第一个比x小的元素，然后用双指针从中心向两边扩展。

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        right = bisect_left(arr, x)
        left = right-1
        for _ in range(k):
            if left < 0:
                right += 1
            elif right >= len(arr) or x-arr[left] <= arr[right]-x:
                left -= 1
            else:
                right += 1
        return arr[left+1: right]


if __name__ == '__main__':
    test = Solution()
    print(test.findClosestElements([1,2,3,4,5], 4, 3))
    print(test.findClosestElements([1,2,3,4,5], 4, -1))
    print(test.findClosestElements([1,2,3,4,5], 2, 3))
        