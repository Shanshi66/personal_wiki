#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int minElements(vector<int>& nums, int limit, int goal) {
        using ltype = long long;
        ltype sum = 0;
        for (const auto& n: nums) {
            sum += n;
        }
        
        ltype diff = goal-sum;
        diff = diff > 0 ? diff : -diff;
        return (diff+(limit-1))/limit;
    }
};