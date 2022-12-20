#include <vector>
#include <iostream>

using namespace std;

//思路：二分答案

class Solution {
public:
    int minimumSize(vector<int>& nums, int maxOperations) {
        int max_num = INT_MIN;
        for (const auto& num: nums) {
            max_num = num > max_num ? num: max_num;
        }
        int l = 1, r = max_num, cost = max_num;
        while (l <= r) {
            int mid = (r-l)/2+l, step = 0;
            for (const auto& num: nums) {
                if (num <= mid) continue;
                step += (num-1)/mid;
            }
            if (step <= maxOperations) {
                cost = mid;
                r = mid-1;
            }
            else {
                l = mid+1;
            }
        }
        return cost;
    }
};

int main() {
    Solution test;
    vector<int> nums{9};
    cout << test.minimumSize(nums, 2) << endl;
}