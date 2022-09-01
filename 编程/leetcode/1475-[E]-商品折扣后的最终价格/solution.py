from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for idx, p in enumerate(prices):
            while stack and p <= prices[stack[-1]]:
                prices[stack[-1]] = prices[stack[-1]]-p
                stack.pop()
            stack.append(idx)
        return prices


if __name__ == '__main__':
    test = Solution()
    print(test.finalPrices([8,4,6,2,3]))
    print(test.finalPrices([1,2,3,4,5]))
    print(test.finalPrices([10,1,1,6]))
        