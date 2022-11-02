import math
from typing import List

# 思路：遍历每个坐标求信号强度，返回最大的那个

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        N = 50
        res = []
        max_q = -1
        for x in range(N+1):
            for y in range(N+1):
                sum_q = 0
                for tower in towers:
                    d = math.sqrt((tower[0]-x)**2+(tower[1]-y)**2)
                    sum_q += math.floor(tower[2]/(1+d)) if d <= radius else 0
                if sum_q > max_q:
                    max_q = sum_q
                    res = [x, y]
        return res

if __name__ == '__main__':
    test = Solution()
    print(test.bestCoordinate([[1,2,5],[2,1,7],[3,1,9]], 2))
    print(test.bestCoordinate([[23,11,21]], 9))
    print(test.bestCoordinate([[1,2,13],[2,1,7],[0,1,9]], 2))
    print(test.bestCoordinate([[42,0,0]], 7))