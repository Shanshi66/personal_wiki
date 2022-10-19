from collections import deque
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        que = deque(students)
        top, cnt = 0, 0
        while que:
            if cnt > len(que):
                break
            st = que.popleft()
            if st == sandwiches[top]:
                top += 1
                cnt = 0
            else:
                que.append(st)
                cnt += 1
        return len(que)

if __name__ == '__main__':
    test = Solution()
    print(test.countStudents([1,1,0,0], [0,1,0,1]))
    print(test.countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))
                