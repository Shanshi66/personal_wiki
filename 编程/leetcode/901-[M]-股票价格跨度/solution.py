
# 思路：单调递减队列，维护当前位置的值及最远的index

class StockSpanner:

    def __init__(self):
        self.idx = 0
        self.st = []


    def next(self, price: int) -> int:
        self.idx += 1
        pre = self.idx
        while self.st and price >= self.st[-1][0]:
            pre = self.st[-1][1]
            self.st.pop()
        self.st.append((price, pre))
        return self.idx-pre+1

if __name__ == '__main__':
    s = StockSpanner()
    print(s.next(100))
    print(s.next(80))
    print(s.next(60))
    print(s.next(70))
    print(s.next(60))
    print(s.next(75))
    print(s.next(85))


        


