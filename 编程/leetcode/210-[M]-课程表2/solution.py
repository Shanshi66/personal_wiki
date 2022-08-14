from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        in_degree = [0]*numCourses
        graph = {}
        for edge in prerequisites:
            graph.setdefault(edge[1], []).append(edge[0])
            in_degree[edge[0]] += 1
        que = []
        for course in range(numCourses):
            if in_degree[course] == 0:
                que.append(course)
        path = []
        while que:
            top = que.pop()
            numCourses -= 1
            path.append(top)
            if top not in graph:
                continue
            for to in graph[top]:
                in_degree[to] -= 1
                if in_degree[to] == 0:
                    que.append(to)
        if numCourses > 0:
            return []
        return path


if __name__ == '__main__':
    test = Solution()
    print(test.findOrder(2, [[1,0]]))
    print(test.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    print(test.findOrder(0, []))
    print(test.findOrder(3, [[1,0], [0,2], [2, 0]]))
    print(test.findOrder(2, []))