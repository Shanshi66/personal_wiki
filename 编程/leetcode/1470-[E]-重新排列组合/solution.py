from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_nums = []
        for i in range(n):
            new_nums.extend([nums[i], nums[i+n]])
        return new_nums


if __name__ == '__main__':
    test = Solution()
    print(test.shuffle([2,5,1,3,4,7], 3))
    print(test.shuffle([1,2,3,4,4,3,2,1], 4))