from tabnanny import check
from typing import List
from wsgiref import validate


class Solution:
    def solve(self, coor_x, coor_y):
        def generate(check_str):
            res = []
            if check_str[0] != '0':
                res.append(check_str)
            if check_str == '0':
                res.append(check_str)
            if check_str[-1] == '0':
                return res
            for i in range(1, len(check_str)):
                if i >= 2 and check_str[0] == '0':
                    continue
                res.append('{}.{}'.format(check_str[0:i], check_str[i:]))
            return res

        res = []
        valid_x = generate(coor_x)
        valid_y = generate(coor_y)
        for x in valid_x:
            for y in valid_y:
                res.append("({}, {})".format(x, y))
        return res
        
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]
        n = len(s)
        result = []
        for i in range(1, n):
            res = self.solve(s[0:i], s[i:])
            result.extend(res)
        return result

if __name__ == '__main__':
    test = Solution()
    print(test.ambiguousCoordinates("(123)"))
    print(test.ambiguousCoordinates("(00011)"))
    print(test.ambiguousCoordinates("(0123)"))
    print(test.ambiguousCoordinates("(100)"))