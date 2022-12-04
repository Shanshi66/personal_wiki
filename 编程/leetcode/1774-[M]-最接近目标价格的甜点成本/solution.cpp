#include<vector>
#include<cmath>
#include<iostream>

using namespace std;

// 思路：搜索+记忆化

class Solution {
public:
    void dfs(vector<int>& top_cost, vector<int>& toppingCosts, int i, int base, int pre, int price) {
        if (i >= 0) top_cost[pre] = price;
        if (i+1 == toppingCosts.size()) return;
        dfs(top_cost, toppingCosts, i+1, base*3, pre+base*0, price);
        dfs(top_cost, toppingCosts, i+1, base*3, pre+base*1, price+toppingCosts[i+1]);
        dfs(top_cost, toppingCosts, i+1, base*3, pre+base*2, price+2*toppingCosts[i+1]);
    }
    int closestCost(vector<int>& baseCosts, vector<int>& toppingCosts, int target) {
        int n = baseCosts.size(), m = toppingCosts.size();
        int ans = INT_MAX;
        vector<int> top_cost(pow(3, m));
        dfs(top_cost, toppingCosts, -1, 1, 0, 0);
        for (const auto& cost: top_cost){
            for (const auto& base: baseCosts) {
                if (abs(cost+base-target) < abs(ans-target)) {
                    ans = cost+base;
                }
                if (abs(cost+base-target) == abs(ans-target) && cost+base < ans) {
                    ans = cost+base;
                }
            }
        }
        return ans;
    }
};

// 官方思路：背包问题，背包容量是target，每个物品可以选0-2次
// can[i][j]表示前i个物品装到容量为j的背包里是否可行，can[i][j] = can[i-1][i-c] | can[i-1][j]

class Solution {
public:
    int closestCost(vector<int>& baseCosts, vector<int>& toppingCosts, int target) {
        int x = *min_element(baseCosts.begin(), baseCosts.end());
        if (x >= target) { //如果基料超过了target，不用加配料了
            return x;
        }
        vector<bool> can(target + 1, false);
        int res = 2 * target - x;
        for (auto& b : baseCosts) {
            if (b <= target) {
                can[b] = true; //初始化
            } else {
                res = min(res, b); // 超过了target，取最小值是最优解
            }
        }
        for (auto& t : toppingCosts) {
            for (int count = 0; count < 2; ++count) { // 技巧，这题结果是“是与否”，或的关系可以传递。第一次循环，i-t可以从i-2t得到，第二次i的状态可以从i-t得到，变相是从i-2t得到
                for (int i = target; i; --i) { // 是状态压缩而来，从后往前遍历是为了保证i-t是前一个状态
                    if (can[i] && i + t > target) { // 本题的特殊情况，总成本可以超过target
                        res = min(res, i + t);
                    }
                    if (i - t > 0) {
                        can[i] = can[i] | can[i - t];
                    }
                }
            }
        }
        for (int i = 0; i <= res - target; ++i) {
            if (can[target - i]) {
                return target - i;
            }
        }
        return res;
    }
};


int main() {
    Solution test;
    
    vector<int> base_cost = {1,7}, toppingCosts = {3,4};
    int target = 10;
    // cout << test.closestCost(base_cost, toppingCosts, target) << endl;
    
    base_cost = {2,3}, toppingCosts = {4,5,100}, target = 18;
    cout << test.closestCost(base_cost, toppingCosts, target) << endl;

    base_cost = {3, 10}, toppingCosts = {2,5}, target = 9;
    // cout << test.closestCost(base_cost, toppingCosts, target) << endl;

    base_cost = {10}, toppingCosts = {1}, target = 1;
    // cout << test.closestCost(base_cost, toppingCosts, target) << endl;
}