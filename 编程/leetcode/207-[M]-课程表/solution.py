from collections import deque
from tabnanny import check
from typing import List

# 思路：遍历每个节点，dfs看这个课程能不能完成

class Solution:
    def check(self, course, check_result, graph):
        if check_result[course] == 2 or course not in graph:
            return True
        if check_result[course] == 1:
            return False
        check_result[course] = 1
        for sub_course in graph[course]:
            if not self.check(sub_course, check_result, graph):
                return False
        check_result[course] = 2
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        graph = {}
        for edge in prerequisites:
            graph.setdefault(edge[0], []).append(edge[1])
        check_result = [0]*numCourses
        for course in range(numCourses):
            if not self.check(course, check_result, graph):
                return False
        return True

# 拓扑排序：从入度为0的点开始bfs，对出节点减度，每次当出节点度数为0的时候，加入队列。最后还有节点没有遍历完时，说明有环，返回false，否则返回true。

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]
        
        for curr, prev in prerequisites:
            indegree[curr] += 1
            adj[prev].append(curr)
        
        que = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                que.append(i)
            
        while que:
            prev = que.popleft()
            numCourses -= 1
            for curr in adj[prev]:
                indegree[curr] -= 1
                if indegree[curr] == 0:
                    que.append(curr)
        
        return not numCourses

if __name__ == '__main__':
    test = Solution()
    print(test.canFinish(2, [[1, 0]]))
    print(test.canFinish(2, [[1,0],[0,1]]))
    print(test.canFinish(5, [[0,1],[1,3], [2,4], [4,2]]))
    print(test.canFinish(6, [[0,1],[1,3], [2,4]]))
            