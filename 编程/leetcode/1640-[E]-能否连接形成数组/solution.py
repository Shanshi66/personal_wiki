from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        nums = {}
        for idx, piece in enumerate(pieces):
            if not piece:
                continue
            nums[piece[0]] = idx
        i = 0
        while i < len(arr):
            if arr[i] in nums:
                j = 0
                idx = nums[arr[i]]
                while j < len(pieces[idx]) and i < len(arr) and arr[i] == pieces[idx][j]:
                    i += 1
                    j += 1
                if j != len(pieces[idx]):
                    return False
            else:
                return False
        return True


if __name__ == '__main__':
    test = Solution()
    print(test.canFormArray([15,88], [[88],[15]]))
    print(test.canFormArray([49,18,16], [[16,18,49]]))
    print(test.canFormArray([91,4,64,78], [[78],[4,64],[91]]))
