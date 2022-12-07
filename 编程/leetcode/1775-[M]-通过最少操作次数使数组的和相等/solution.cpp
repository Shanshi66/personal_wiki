#include<vector>
#include<iostream>

using namespace std;

// 思路：遍历每个可能的和，看最快的步骤是做少。如果数组和要增加，从最小值开始增加是最快的。如果数组和要减少，从最大值开始减少是最快的。

class Solution {
public:
    int minOperations(vector<int>& nums1, vector<int>& nums2) {
        int size1 = nums1.size(), size2 = nums2.size();
        if (size1 > size2 && 6*size2 < size1) {
            return -1;
        }
        if (size2 > size1 && 6*size1 < size2) {
            return -1;
        }
        vector<int> stat1(6, 0), stat2(6, 0);
        int sum1 = 0, sum2 = 0;
        for (auto& x: nums1) {
            stat1[x-1] += 1;
            sum1 += x;
        }
        for (auto& x: nums2) {
            stat2[x-1] += 1;
            sum2 += x;
        }
        if (sum1 > sum2) {
            swap(stat1, stat2);
            swap(sum1, sum2);
        }
        int ans = size1+size2;
        for (int i = sum1; i <= sum2; i++) {
            int step = 0, diff = i-sum1, j = 0;
            while (diff > 0 && j < 6) {
                if (diff > stat1[j]*(6-j-1)) {
                    diff -= stat1[j]*(6-j-1);
                    step += stat1[j];
                }
                else {
                    step += diff/(6-j-1);
                    if (diff%(6-j-1) > 0) {
                        step += 1;
                    }
                    diff = 0;
                }
                j += 1;
            }
            if (diff > 0) { // 注意不可能达到的情况！！
                continue;
            }
            diff = sum2-i, j = 5;
            while (diff > 0 & j >= 0) {
                if (diff > stat2[j]*j) {
                    diff -= stat2[j]*j;
                    step += stat2[j];
                }
                else {
                    step += diff/j;
                    if (diff%j > 0) {
                        step += 1;
                    }
                    diff = 0;
                }
                j -= 1;
            }
            if (diff > 0) {
                continue;
            }
            ans = min(ans, step);
        }
        return ans;
    }
};

// 官方思路：先计算diff，假设sum(s1) < sum(s2)，那么s1里数增加，s2里数减小。
// 每个数的贡献度可以计算，从最高贡献度的数开始较少diff，知道diff=0；

class Solution {
public:
    int help(vector<int>& h1, vector<int>& h2, int diff) {
        vector<int> h(7, 0); // 贡献度存储，从0-5；
        for (int i = 1; i < 7; ++i) {
            h[6 - i] += h1[i];
            h[i - 1] += h2[i];
        }
        int res = 0;
        for (int i = 5; i && diff > 0; --i) {
            int t = min((diff + i - 1) / i, h[i]); // 妙，diff+i-1/i可以实现取floor的效果
            res += t;
            diff -= t * i;
        }
        return res;
    }

    int minOperations(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size(), m = nums2.size();
        if (6 * n < m || 6 * m < n) {
            return -1;
        }
        vector<int> cnt1(7, 0), cnt2(7, 0);
        int diff = 0;
        for (auto& i : nums1) {
            ++cnt1[i];
            diff += i;
        }
        for (auto& i : nums2) {
            ++cnt2[i];
            diff -= i;
        }
        if (!diff) {
            return 0;
        }
        if (diff > 0) {
            return help(cnt2, cnt1, diff);
        }
        return help(cnt1, cnt2, -diff);
    }
};

int main() {
    Solution test;
    vector<int> s1{1,2,3,4,5,6}, s2{1,1,2,2,2,2};
    cout << test.minOperations(s1, s2) << endl;

    vector<int> s3{1,1,1,1,1,1,1}, s4{6};
    cout << test.minOperations(s3, s4) << endl;

    vector<int> s5{6,6}, s6{1};
    cout << test.minOperations(s5, s6) << endl;

}