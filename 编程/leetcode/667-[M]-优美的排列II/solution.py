from typing import List


# 思路：最大的K区间是1，n，2，n-1,...。当有k-1个不同的数时，可以做大让最后的所有区间间隔都是1

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        answer = [1]
        step = 0
        i = 2
        j = n
        for _ in range(n-1):
            if step == k-1:
                break
            if step&1:
                answer.append(i)
                i += 1
            else:
                answer.append(j)
                j -= 1
            step += 1
        if step&1:
            answer.extend(range(j, i-1, -1))
        else:
            answer.extend(range(i, j+1))
        return answer



if __name__ == '__main__':
    test = Solution()
    print(test.constructArray(3, 1))
    print(test.constructArray(3, 2))
    print(test.constructArray(10, 2))
    print(test.constructArray(10, 3))
    print(test.constructArray(10, 9))
    print(test.constructArray(2, 1))
        