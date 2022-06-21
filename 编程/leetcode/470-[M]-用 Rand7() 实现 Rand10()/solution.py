# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

import random

def rand7():
    return random.randint(1,7)


# 构造一个生成序列，取其中概率相同的元素，其他拒绝(拒绝采样)。
# 期望值：第一轮有40/49的概率被采纳，9/49的概率被拒绝。expect = 2 + 2*9/49 + 2*(9/49)^2 ... = 2.45
# 如何最优：每一次拒绝不丢弃，第一次剩余40-49这9个数字，实际就是rand9。问题变成利用rand9和rand7生成rand10，以此类推。

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            i = 7*(rand7()-1)+rand7()-1
            if i > 39:
                continue
            return i//4+1

def rand(n):
    times = {}
    test = Solution()
    for i in range(n):
        j = test.rand10()
        times.setdefault(j, 0)
        times[j] += 1
    print(times)

if __name__ == '__main__':
    rand(1000)
    

    
