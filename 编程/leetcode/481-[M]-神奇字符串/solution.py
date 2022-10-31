from lib2to3.pgen2.token import SLASHEQUAL


class Solution:
    def magicalString(self, n: int) -> int:
        res = 0
        s = '122'
        flag = '1'
        i = 2
        while len(s) < n:
            s += flag*int(s[i])
            i += 1
            flag = '1' if flag == '2' else '2'
        res = 0
        for i in range(n):
            if s[i] == '1':
                res += 1
        return res

if __name__ == '__main__':
    test = Solution()
    print(test.magicalString(6))
    print(test.magicalString(1))
        