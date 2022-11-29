#include<string>
#include<iostream>

using namespace std;

//思路：动态规划，dp[i][0]表示第i个位置不变保证前i个字符满足条件的步数，dp[i][0]表示第i个位置变保证前i个字符满足条件的步数。因为i只依赖i-1，可以压缩空间。

class Solution {
public:
    int minOperations(string s) {
        int n = s.size();
        int pre_0 = 0, pre_1 = 1;
        for (int i = 1; i < n; i++) {
            if (s[i] == s[i-1]) {
                int tmp = pre_0;
                pre_0 = pre_1;
                pre_1 = tmp+1;
            } else {
                pre_1 = pre_1+1;
            }
        }
        return pre_0>pre_1?pre_1:pre_0;
    }
};

int main() {
    Solution test;
    cout << test.minOperations("0100") << endl;
}