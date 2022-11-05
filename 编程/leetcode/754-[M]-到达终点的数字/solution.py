import math

# 思路：
# target < 0的情况可以转化为target > 0的情况
# 可以求出第一次前n个数和大于target的情况，每次可以其中任意两个数的和变成1(变成-1也行，但是只需要考虑1的情况，因为-1相当于变换2个数改变符号，使得总和-1，x+x+1+1=x+x+2)
# x+x+1-1=(n+1)*n/2-target=diff=2x，即如果diff是偶数，将x变成负号即可。否则，如果下一个数是奇数，可以再加一步使得diff变成偶数。否则可以加2步。

class Solution:
    def reachNumber(self, target: int) -> int:
        if target < 0:
            target = -target
        n = math.ceil((-1+math.sqrt(1+8*target))/2)
        diff = n*(n+1)//2-target
        if not diff&1:
            return n
        if (n+1)&1: 
            # 包括特殊情况：前n-1个数的和等于target-1
            # 因为走到这一步diff为奇数，这种情况下diff等于n+1
            return n+1
        return n+2



if __name__ == '__main__':
    test = Solution()
    # print(test.reachNumber(1))
    # print(test.reachNumber(2))
    # print(test.reachNumber(3))
    # print(test.reachNumber(4))
    # print(test.reachNumber(5))
    # print(test.reachNumber(6))
    # print(test.reachNumber(7))
    # print(test.reachNumber(8))
    # print(test.reachNumber(9))
    # print(test.reachNumber(10))
    # print(test.reachNumber(11))
    # print(test.reachNumber(12))
    print(test.reachNumber(16))
