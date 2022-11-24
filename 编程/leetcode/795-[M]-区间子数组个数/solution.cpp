#include<iostream>
#include<vector>
#include<stack>

using namespace std;

// 思路：枚举每个数为最大值的序列个数，并求和
// left_max[i]表示截止到i并i为最大值的最长子序列左边界，right_max[i]表示以i为起始并且为最大值的右边界
// 需要注意的是，会存在相同值导致重复计算情况，发现只要枚举到i时，j<i 且 nums[i]==nums[j]是，这种情况已经被考虑过，因此求左边界忽略相同值即可。

class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& nums, int left, int right) {
        int n = nums.size();
        stack<int> st;
        vector<int> left_max(n), right_max(n);
        for (int i=0; i<n; i++) {
            left_max[i] = i;
            right_max[i] = i;
        }

        for (int i=0; i<n; i++) {
            while (!st.empty() && nums[i] > nums[st.top()]) {
                left_max[i] = left_max[st.top()];
                st.pop();
            } 
            st.push(i);
        }
        
        while(!st.empty()) st.pop();

        for (int i=n-1; i>=0; i--) {
            while (!st.empty() && nums[i] >= nums[st.top()]) {
                right_max[i] = right_max[st.top()];
                st.pop();
            }
            st.push(i);
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] < left || nums[i] > right) {
                continue;
            }
            ans += (i-left_max[i]+1)*(right_max[i]-i+1);
        }
        return ans;
    }
};


// 官方思路1：
// num中的数可以分成3类：0-(-, left), 1-[left, right], 2-(right, +)
// 那么结果中必须包含至少一个1，不能有2
// 遍历每一个数，如果是0/1，以这个数为右端点，左端点可以在最近一个1和2之间

class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& nums, int left, int right) {
        int res = 0, last2 = -1, last1 = -1;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] >= left && nums[i] <= right) {
                last1 = i;
            } else if (nums[i] > right) {
                last2 = i;
                last1 = -1;
            }
            if (last1 != -1) {
                res += last1 - last2;
            }
        }
        return res;
    }
};

// 官方思路2：
// 同思路1将num的数分成3类，问题的答案是，只包含0或1的区间数量-只包含0的区间数量

class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& nums, int left, int right) {
        return count(nums, right) - count(nums, left - 1);
    }

    int count(vector<int>& nums, int lower) {
        int res = 0, cur = 0;
        for (auto x : nums) {
            cur = x <= lower ? cur + 1 : 0;
            res += cur; //以当前元素为结尾的序列数量有cur个
        }
        return res;
    }
};

int main() {
    Solution test;
    // vector<int> v1{2,1,4,3};
    // cout << test.numSubarrayBoundedMax(v1, 2, 3) << endl;
    // vector<int> v2{2,9,2,5,6};
    // cout << test.numSubarrayBoundedMax(v2, 2, 8) << endl;
    vector<int> v3{2,1,3,2,3,1,3,4,5};
    cout << test.numSubarrayBoundedMax(v3, 3, 10) << endl;
}