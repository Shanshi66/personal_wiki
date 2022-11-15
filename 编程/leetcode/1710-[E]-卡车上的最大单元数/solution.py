from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])
        ans = 0
        for box in boxTypes:
            if truckSize == 0:
                break
            if box[0] <= truckSize:
                ans += box[0]*box[1]
                truckSize -= box[0]
            else:
                ans += truckSize*box[1]
                truckSize = 0
        return ans


if __name__ == '__main__':
    test = Solution()
    print(test.maximumUnits([[1,3],[2,2],[3,1]], 4))
    print(test.maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))