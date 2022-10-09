# 青娃回家
# 给长度为n的数组，数组上每个位置都为不大于n的整数，其中可能会有值为-1的值，代表到家。
# 在任意位置，有3个选择：
# 1. 按下标数值跳到指定位置，比如值为3，则跳到数据下标为3的位置
# 2. 向左跳一步
# 3. 向右跳一步
# 4. 如果值为-1，表示到家
# 求回家最小步数

from collections import deque

class Solution:
    def backHome(self, steps):
        if len(steps) <= 1:
            return 0
        que = deque([(0, 0)])
        vis = [False]*len(steps)
        vis[0] = False
        while que:
            idx, st = que.popleft()
            if steps[idx] == -1:
                return st
            if not vis[steps[idx]]:                
                que.append((steps[idx], st+1))
                vis[steps[idx]] = True
            if idx+1 < len(steps) and not vis[idx+1]:
                que.append((idx+1, st+1))
                vis[idx+1] = True
            if idx-1 >= 0 and not vis[idx-1]:
                que.append((idx-1, st+1))
                vis[idx-1] = True
        return -1


if __name__ == '__main__':
    test = Solution()
    print(test.backHome([-1,0,2]))
    print(test.backHome([1,-1,2]))
    print(test.backHome([0,1,2]))
    print(test.backHome([0,3,2,-1]))