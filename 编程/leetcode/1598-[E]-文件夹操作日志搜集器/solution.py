from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        deepth = 0
        for log in logs:
            if log == '../':
                deepth = deepth-1 if deepth > 0 else deepth
            elif log == './':
                continue
            else:
                deepth += 1
        return deepth



if __name__ == '__main__':
    test = Solution()
    print(test.minOperations(["./","wz4/","../","mj2/","../","../","ik0/","il7/"]))