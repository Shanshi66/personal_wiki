# 思路：找规律，最终的字符串f(n) = f(n-1) + reverse(f(n-1))，reverse表示将1变成0,0变成1。反过来即可求解。

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        if n > 1 and k == 2:
            return 1 
        if k <= 2**(n-2):
            return self.kthGrammar(n-1, k)
        else:
            return 1-self.kthGrammar(n-1, k-2**(n-2))


if __name__ == '__main__':
    test = Solution()
    print(test.kthGrammar(1, 1))
    print(test.kthGrammar(2, 1))
    print(test.kthGrammar(2, 2))
    print(test.kthGrammar(10, 100))