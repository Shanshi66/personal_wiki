import math

# 推理思路

# 1. target < 0的情况可以转化为target > 0的情况
# 2. 可以求出第一次前n个数和大于target的n，以两个元素为1组，每次改变相邻的两个数符号使和从$x+x+1$变成$-x+x+1=1$，原始和与改变之后的和diff是$x+x+1-1=2x=(n+1)n/2-target$，即$diff=2x$。（将相邻的两个数变成$x-(x+1)=-1$是等价的，因为$diff=2x+2$，奇偶性不变）
# 3. 根据2的结论，如果diff是偶数，将$x$变成负号即可。否则，如果下一个数是奇数，可以再加一步使得新diff变成偶数。否则可以加2步，是diff变成偶数。

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
