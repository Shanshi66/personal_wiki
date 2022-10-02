# 思路：双指南针，分别找start和end中对应的L和R前后关系是否对，L只能向左移，因此在start中出现的位置一定靠后。R相反。

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        n, m = len(start), len(end)
        if n != m:
            return False
        i, j = 0, 0
        while i < n:
            if end[i] == 'X':
                i += 1
                continue
            if end[i] == 'L':
                while j < n and start[j] == 'X': j += 1
                if j < n and start[j] == 'L' and j >= i:
                    i += 1
                    j += 1
                    continue
                else:
                    return False
            if end[i] == 'R':
                while j < n and start[j] == 'X': j += 1
                if j < n and start[j] == 'R' and j <= i:
                    j += 1
                    i += 1
                    continue
                else:
                    return False
        while j < n and start[j] == 'X': j += 1
        if j < n:
            return False
        return True


if __name__ == '__main__':
    test = Solution()
    print(test.canTransform("RXXLRXRXL", "XRLXXRRLX"))
    print(test.canTransform("RXLR", "RXLR"))
    print(test.canTransform("LXXLXRLXXL","XLLXRXLXLX"))
    print(test.canTransform("RXXLRXRXL","XRLXXRRLX"))
    print(test.canTransform("XXL", "LXX"))
    print(test.canTransform("XLLR", "LXLX"))
    print(test.canTransform("XLXRRXXRXX","LXXXXXXRRR"))
                


