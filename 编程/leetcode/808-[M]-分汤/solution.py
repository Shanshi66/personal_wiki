class Solution:
    def solve(self, Aml, Bml):
        if Aml <= 0 and Bml > 0:
            return 1
        if Aml <= 0 and Bml <= 0:
            return 0.5
        if Bml <= 0:
            return 0
        return 0.25*(self.solve(Aml-100, Bml)+
                     self.solve(Aml-75, Bml-25)+
                     self.solve(Aml-50, Bml-50)+
                     self.solve(Aml-25, Bml-75))
        
    def soupServings(self, n: int) -> float:
        p = self.solve(n, n)
        return p

if __name__ == "__main__":
    test = Solution()
    # for i in range(1, 500):
        # print(i, test.soupServings(i))
    print(test.soupServings(50))
    print(test.soupServings(100))
    print(test.soupServings(1000))