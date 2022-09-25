from enum import Flag
from unicodedata import digit


class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans = 0
        nc_num = set([0,1,8])
        c_num = set([2,5,6,9])
        for i in range(1, n+1):
            is_c = False
            is_e = True
            while i:
                digit = i%10
                i = i//10
                if digit in c_num:
                    is_c = True
                elif digit in nc_num:
                    continue
                else:
                    is_e = False
                    break
            if is_c and is_e:
                ans += 1
        return ans 
                

        