from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0]*n
        if k == 0:
            return result
        cum_sum = [x for x in code]
        for i in range(n):
            if i > 0:
                cum_sum[i] = cum_sum[i-1]+code[i]
        for i in range(n):
            if k > 0:
                result[i] = cum_sum[i+k]-cum_sum[i] if i+k < n else cum_sum[n-1]-cum_sum[i]+cum_sum[(i+k)%n]
            if k < 0:
                result[i] = cum_sum[i-1]-cum_sum[i+k-1] if i+k-1 >= 0 or i == 0 else cum_sum[n-1]-cum_sum[i+k-1]+cum_sum[i-1]
        return result


if __name__ == '__main__':
    test = Solution()
    print(test.decrypt([5,7,1,4], 3))
    print(test.decrypt([2,4,9,3], -2))
    print(test.decrypt([2,1,3,4,5,2], -1))
