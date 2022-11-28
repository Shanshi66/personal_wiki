#include<vector>
#include<iostream>

using namespace std;

class Solution {
public:
    bool check(vector<int>& nums) {
        int n = nums.size(), inc_cnt = 0;
        if (n <= 1) {
            return true;
        }
        inc_cnt = 1;
        for (int i = 0; i < n-1; i++) {
            if (nums[i] > nums[i+1]) {
                inc_cnt += 1;
            }
        }
        if (inc_cnt == 2 && nums[n-1] <= nums[0]) {
            return true;
        }
        if (inc_cnt == 1) {
            return true;
        }
        return false;
    }
};

int main() {
    Solution test;
    vector<int> v{3,4,5,1,2};
    cout << test.check(v) << endl;
    vector<int> v1{2,1,3,4};
    cout << test.check(v1) << endl;
    vector<int> v2{1,2,3};
    cout << test.check(v2) << endl;
}