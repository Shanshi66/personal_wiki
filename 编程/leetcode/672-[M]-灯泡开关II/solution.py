class Solution:

    def operate(self, s, ith):
        n = len(s)
        if ith == 1:
            for i in range(n):
                s[i] = '0' if s[i] == '1' else '1'
        if ith == 2:
            for i in range(1, n, 2):
                s[i] = '0' if s[i] == '1' else '1'
        if ith == 3:
            for i in range(0, n, 2):
                s[i] = '0' if s[i] == '1' else '1'
        if ith == 4:
            for i in range(0, n, 3):
                s[i] = '0' if s[i] == '1' else '1'
        return s

    def solve(self, n, presses):
        ori = ['1']*n
        def dfs(press_left, l, r):
            if press_left == 0:
                self.result_set.add(''.join(ori))
                return
            if press_left > r-l+1:
                return
            for i in range(l, r+1):
                self.operate(ori, i)
                dfs(press_left-1, l+1, r)
                self.operate(ori, i)
        dfs(presses, 1, 4)

    def flipLights(self, n: int, presses: int) -> int:
        self.result_set = set()
        if presses == 0:
            self.solve(n, 0)
        elif presses == 1:
            self.solve(n, 1)
        elif presses == 2:
            self.solve(n, 0)
            self.solve(n, 2)
        elif presses&1:
            self.solve(n, 1)
            self.solve(n, 3)
        else:
            self.solve(n, 0)
            self.solve(n, 2)
            self.solve(n, 4)
        return len(self.result_set)


if __name__ == '__main__':
    test = Solution()
    print(test.flipLights(1, 1))
    print(test.flipLights(2, 1))
    print(test.flipLights(3, 1))
    print(test.flipLights(100, 3))