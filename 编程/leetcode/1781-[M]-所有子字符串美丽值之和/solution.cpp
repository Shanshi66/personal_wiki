#include <string>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int beautySum(string s) {
        int n = s.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            int count[26] = {0};
            for (int j = i; j < n; j++) {
                count[s[j]-'a'] += 1;
                int min_freq = INT_MAX, max_freq = -1;
                for (int k = 0; k < 26; k++) {
                    if (count[k] == 0) {
                        continue;
                    }
                    min_freq = min_freq > count[k] ? count[k]: min_freq;
                    max_freq = max_freq < count[k] ? count[k]: max_freq;
                }
                ans += max_freq-min_freq;
            }
        }
        return ans;
    }
};