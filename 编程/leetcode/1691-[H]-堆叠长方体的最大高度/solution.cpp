#include <vector>
#include <iostream>

using namespace std;

// 思路：动态规划，每个长方体的任意一条边都可以成为高，枚举高的每一种可能性，从大到小排序。问题转化成从这个新序列中找出和最大的子序列。
// dp[i][j]表示以第i个长方体为结尾的最大高度和，j \in {0,1}，表示长和宽的旋转的两种状态。

class Solution {
public:
    int maxHeight(vector<vector<int>>& cuboids) {
        using tuple_type = tuple<int, int, int, int>;
        int n = cuboids.size(), m = n*3;
        vector<tuple_type> cub_list(m);
        for (int i = 0; i < n; i++) {
            // 需要对序列排序，让大的宽或高排在前面
            sort(cuboids[i].begin(), cuboids[i].end(), std::greater<int>()); 
            cub_list[i*3] = make_tuple(cuboids[i][0], cuboids[i][1], cuboids[i][2], i);
            cub_list[i*3+1] = make_tuple(cuboids[i][1], cuboids[i][0], cuboids[i][2], i);
            cub_list[i*3+2] = make_tuple(cuboids[i][2], cuboids[i][0], cuboids[i][1], i);
        }
        sort(cub_list.begin(), cub_list.end(), [](const tuple_type& a, const tuple_type& b){
            if (get<0>(a) != get<0>(b)) {
                return get<0>(a) > get<0>(b);
            }
            else if (get<1>(a) != get<1>(b)){
                return get<1>(a) > get<1>(b);
            } 
            else {
                return get<2>(a) > get<2>(b);
            }
        });
        vector<vector<int>> dp(m, vector<int>(2));
        int ans = 0;
        for (int i = 0; i < m; i++) {
            dp[i][0] = get<0>(cub_list[i]);
            dp[i][1] = get<0>(cub_list[i]);
            int tmp = 0;
            for (int j = 0; j < i; j++) {
                //相同的长方体跳过
                if (get<3>(cub_list[i]) == get<3>(cub_list[j])) {
                    continue;
                }
                if (get<1>(cub_list[i]) <= get<1>(cub_list[j]) &&
                    get<2>(cub_list[i]) <= get<2>(cub_list[j])) {
                        dp[i][0] = max(dp[i][0], dp[j][0]+get<0>(cub_list[i]));
                    }
                if (get<1>(cub_list[i]) <= get<2>(cub_list[j]) &&
                    get<2>(cub_list[i]) <= get<1>(cub_list[j])) {
                        dp[i][0] = max(dp[i][0], dp[j][1]+get<0>(cub_list[i]));
                    }
                if (get<2>(cub_list[i]) <= get<1>(cub_list[j]) &&
                    get<1>(cub_list[i]) <= get<2>(cub_list[j])) {
                        dp[i][1] = max(dp[i][1], dp[j][0]+get<0>(cub_list[i]));
                    }
                if (get<2>(cub_list[i]) <= get<2>(cub_list[j]) &&
                    get<1>(cub_list[i]) <= get<1>(cub_list[j])) {
                        dp[i][1] = max(dp[i][1], dp[j][1]+get<0>(cub_list[i]));
                    }
            }
            ans = max(ans, dp[i][0]);
            ans = max(ans, dp[i][1]);
        }
        return ans;
    }
};

//官方思路：如果长方体(l1,w1,h1) < (l1,w1,h1)，可以证明每个长方体长宽高按从小到大排序后也满足条件。用最大的边做高，问题转化为dp问题。

int main() {
    Solution test;
    vector<vector<int>> test1{{50,45,20},{95,37,53},{45,23,12}};
    // cout << test.maxHeight(test1) << endl;

    test1 = vector<vector<int>>{{67,48,27},{26,9,68},{31,67,63}};
    cout << test.maxHeight(test1) << endl;
}