from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        p_pop = 0
        for num in pushed:
            stack.append(num)
            while stack and p_pop < len(popped) and stack[-1] == popped[p_pop]:
                stack.pop()
                p_pop += 1
        if p_pop == len(popped):
            return True
        return False



if __name__ == '__main__':
    test = Solution()
    print(test.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
    print(test.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))
    print(test.validateStackSequences([1], [1]))
    print(test.validateStackSequences([1], [2]))
        