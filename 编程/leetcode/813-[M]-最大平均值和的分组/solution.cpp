#include<vector>
#include<iostream>

using namespace std;

class Solution {
public:
    double largestSumOfAverages(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> cumulate(nums);
        for (int i = 1; i < n; i++) {
            cumulate[i] = cumulate[i]+cumulate[i-1];
        }
        
        vector<vector<double>> dp(n, vector<double>(k+1));
        
        for (int i = 0; i < n; i++) {
            dp[i][1] = cumulate[i]*1.0/(i+1);
        }
        for (int i = 1; i < n; i++) {
            for (int j = 2; j <= k; j++) {
                for (int t = 0; t < i; t++) {
                    double tmp = dp[t][j-1]+(cumulate[i]-cumulate[t])*1.0/(i-t);
                    dp[i][j] = tmp > dp[i][j] ? tmp:dp[i][j];
                }
            }
        }
        return dp[n-1][k];
    }
};

int main() {
    Solution test;
    vector<int> nums{9,1,2,3,9};
    cout << test.largestSumOfAverages(nums, 3) << endl;
    nums = vector<int>{1,2,3,4,5,6,7};
    cout << test.largestSumOfAverages(nums, 4) << endl;
}