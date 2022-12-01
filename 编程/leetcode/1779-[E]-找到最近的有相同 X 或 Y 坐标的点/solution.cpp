#include<vector>
#include<iostream>

using namespace std;

class Solution {
public:
    int nearestValidPoint(int x, int y, vector<vector<int>>& points) {
        int min_dist = INT_MAX, N = points.size(), min_index = -1;
        for (int i = 0; i < N; i++) {
            if (x == points[i][0] || y == points[i][1]) {
                int dist = abs(points[i][0]-x)+abs(points[i][1]-y);
                if (dist < min_dist) {
                    min_dist = dist;
                    min_index = i;
                } 
            }
        }
        return min_index;
    }
};

int main() {
    Solution test;
    vector<vector<int>> p{{1,2},{3,1},{2,4},{2,3},{4,4}};
    cout << test.nearestValidPoint(3,4,p) << endl;
}