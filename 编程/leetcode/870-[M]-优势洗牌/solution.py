from typing import List
import bisect


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums1.sort()
        flag = [False]*n
        new_nums2 = list(enumerate(nums2))
        new_nums2.sort(key = lambda x: x[1])
        i, j = 0, 0
        res = []
        for k in range(n):
            while i < n and (nums1[i] <= new_nums2[k][1] or flag[i]): i+=1
            if i < n:
                res.append((new_nums2[k][0], nums1[i]))
                flag[i] = True
                i += 1
            else:
                while j < n and flag[j]: j += 1
                if j < n: 
                    res.append((new_nums2[k][0], nums1[j]))
                    flag[j] = True
                    j += 1
        res.sort(key = lambda x: x[0])
        return [x[1] for x in res]
                
        


if __name__ == '__main__':
    test = Solution()
    print(test.advantageCount([2,7,11,15], [1,10,4,11]))
    print(test.advantageCount([12,24,8,32], [13,25,32,11]))
    print(test.advantageCount([4,2,5,6,7], [2,3,4,1,5]))

        