import bisect
from typing import List

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], x[1]))
        intervals_left = [x[0] for x in intervals]
        print(intervals)
        n = len(intervals)
        count = 0
        vis = [False]*n
        for i in range(n):
            if vis[i]:
                continue
            count += 1
            vis[i] = True
            target = i
            j = target+1
            while True:
                while j < n and vis[j]: j+=1
                if j >= n:
                    break
                idx = bisect.bisect_right(intervals_left, intervals[target][1], lo = j)
                if idx >= n:
                    break
                vis[idx] = True
                target = idx
                j = target+1
        return count


if __name__ == '__main__':
    test = Solution()
    # print(test.minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))
    case = [[229966,812955],[308778,948377],[893612,952735],[395781,574123],[478514,875165],[766513,953839],[460683,491583],[133951,212694],[376149,838265],[541380,686845],[461394,568742],[804546,904032],[422466,467909],[557048,758709],[680460,899053],[110928,267321],[470258,650065],[534607,921875],[292993,994721],[645020,692560],[898840,947977],[33584,330630],[903142,970252],[17375,626775],[804313,972796],[582079,757160],[785002,987823],[599263,997719],[486500,527956],[566481,813653],[211239,863969],[808577,883125],[21880,516436],[264747,412144],[327175,772333],[984807,988224],[758172,916673],[23583,406006],[954674,956043],[379202,544291],[688869,785368],[841735,983869],[99836,916620],[332504,740696],[740840,793924],[896607,920924],[868540,922727],[125849,550941],[433284,685766]]
    min_left = min([x[0] for x in case])
    case = [[x[0]-min_left, x[1]-min_left] for x in case]
    # print(len(case))
    print(test.minGroups(case))
    # print(test.minGroups([[1,3],[5,6],[8,10],[11,13]]))
    # print(test.minGroups([[1,10],[2,9],[3,8],[4,7]]))
    # print(test.minGroups([[1,10]]))
        