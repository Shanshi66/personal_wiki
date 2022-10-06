from typing import List

# 思路：将1平分，因为数组末尾的0是确定的，因此每个part的形式是确定的。

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        one_num = sum([1 if x == 1 else 0 for x in arr])
        if one_num == 0:
            return [0, 2]
        if one_num%3:
            return [-1, -1]
        one_num_per = one_num//3
        zero_behind = 0
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 0:
                zero_behind += 1
            else:
                break
        index = []
        ones, zeros = 0, 0
        for i, x in enumerate(arr):
            if ones == one_num_per and zeros == zero_behind:
                index.append(i)
                ones = 0
                zeros = 0
            if x == 1:
                if ones < one_num_per:
                    ones += 1
                elif zeros < zero_behind:
                    return [-1, -1]
            else:
                if ones == one_num_per and zeros < zero_behind:
                    zeros += 1
        if len(index) < 2:
            return [-1, -1]
        
        i, j, k = 0, index[0], index[1]
        while i < index[0] and arr[i] == 0: i += 1
        while j < index[1] and arr[j] == 0: j += 1
        while k < len(arr) and arr[k] == 0: k += 1
        while k < len(arr):
            if arr[i] == arr[j] and arr[j] == arr[k]:
                i += 1
                j += 1
                k += 1
            else:
                return [-1, -1]
        return [index[0]-1, index[1]]


if __name__ == '__main__':
    test = Solution()
    print(test.threeEqualParts([1,0,1,0,1]))
    print(test.threeEqualParts([1,1,0,0,1]))
    print(test.threeEqualParts([1,1,0,1,1]))
    print(test.threeEqualParts([1,1,0,0,1,1,0,0,1,1,0]))
    print(test.threeEqualParts([1,1,1,1]))
    print(test.threeEqualParts([1,1,1]))
    print(test.threeEqualParts([0,0,0,0]))