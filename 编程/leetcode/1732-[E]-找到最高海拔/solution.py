from cmath import inf
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        h = 0
        res = h
        for g in gain:
            h = h+g
            res = max(res, h)
        return res