#include<iostream>
#include<vector>
#include<string>

using namespace std;

// 思路：动态规划，one_num[i]表示左边/右边1的个数，steps[i]表示左边/右边所有的球移动到i个位置需要的步数

class Solution {
public:
    vector<int> minOperations(string boxes) {
        int n = boxes.size();
        vector<int> ans(n);
        
        int one_num = 0, steps = 0;
        for (int i = 1; i < n; i++) {
            if (boxes[i-1] == '1') {
                one_num += 1;
            }
            steps += one_num;
            ans[i] += steps;
        }

        one_num = 0;
        steps = 0;
        for (int i = n-2; i >= 0; i--) {
            if (boxes[i+1] == '1') {
                one_num += 1;
            }
            steps += one_num;
            ans[i] += steps;
        }
        return ans;
    }
};
