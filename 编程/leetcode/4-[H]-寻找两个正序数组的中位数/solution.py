# 以数组末尾最小的数字为target，在另一个数组中找第一个比它大的数，然后划分子问题
# 平均情况log(m)+log(n)，最坏情况O(m+n)

class Solution(object):
    def findFirstBigger(self, num, s, e, target):
        if s >= e:
            return s
        mid = (s+e)//2
        if num[mid] <= target:
            idx = self.findFirstBigger(num, mid+1, e, target)
        else:
            idx = self.findFirstBigger(num, s, mid, target)
        return idx

    def work_wrapper(self, nums1, s1, e1, nums2, s2, e2, k):
        if nums1[e1] >= nums2[e2]:
            return self.work(nums2, s2, e2, nums1, s1, e1, k)
        else:
            return self.work(nums1, s1, e1, nums2, s2, e2, k)

    def work(self, nums1, s1, e1, nums2, s2, e2, k):
        if k == 1:
            return (max(nums1[e1], nums2[e2-1]), nums2[e2]) if e2 > 0 else (nums1[e1], nums2[e2])
        target = nums1[e1]
        idx = self.findFirstBigger(nums2, s2, e2, target)
        bigger_num = e2-idx+1
        if bigger_num > k:
            index = e2-k+1
            return nums2[index-1], nums2[index]
        elif bigger_num == k:
            return target, nums2[idx]
        else:
            if idx-1 >=0:
                return self.work_wrapper(nums1, s1, e1, nums2, s2, idx-1, k-bigger_num)
            else:
                index = e1-(k-bigger_num)+1
                return nums1[index-1], nums1[index]

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len = len(nums1)+len(nums2)
        k = total_len//2
        if len(nums1) == 0 and len(nums2) == 0:
            return 0
        elif len(nums1) == 0:
            return nums2[len(nums2)//2] if len(nums2)&1 else (nums2[len(nums2)//2]+nums2[len(nums2)//2-1])/2
        elif len(nums2) == 0:
            return nums1[len(nums1)//2] if len(nums1)&1 else (nums1[len(nums1)//2]+nums1[len(nums1)//2-1])/2
        a, b = self.work_wrapper(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, k)
        return a if total_len&1 else (a+b)/2


class Solution1(object):
    def findMedianSortedArrays(self, nums1, nums2):
        


if __name__ == '__main__':
    s = Solution()
    # nums1 = [1,3]
    # nums2 = [2]
    # res = s.findMedianSortedArrays(nums1, nums2)
    # print(res)
    # nums1 = [1,2]
    # nums2 = [3,4]
    # res = s.findMedianSortedArrays(nums1, nums2)
    # print(res)
    # nums1 = [1,3,6,7,9]
    # nums2 = [2,2,3,5]
    # res = s.findMedianSortedArrays(nums1, nums2)
    # print(res)
    # nums1 = [1]
    # nums2 = [2]
    # res = s.findMedianSortedArrays(nums1, nums2)
    # print(res)
    # nums1 = [1,2]
    # nums2 = [-1,3]
    # res = s.findMedianSortedArrays(nums1, nums2)
    # print(res)
    nums1 = [4]
    nums2 = [1,2,3]
    res = s.findMedianSortedArrays(nums1, nums2)
    print(res)

        
        
        