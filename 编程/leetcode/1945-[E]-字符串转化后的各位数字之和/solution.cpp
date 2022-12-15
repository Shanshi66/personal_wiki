#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    int getLucky(string s, int k) {
        string new_s;
        for (const auto& c: s) {
            new_s += to_string(c-'a'+1);
        }
        while (k--) {
            if (new_s.size() == 1) {
                break;
            }
            int sum = 0;
            for (const auto& c: new_s) {
                sum += c-'0';
            }
            new_s = to_string(sum);
        }
        return stoi(new_s);
    }
};

int main() {
    Solution test;
    cout << test.getLucky("iiii", 1) << endl;
    cout << test.getLucky("leetcode", 2) << endl;
    cout << test.getLucky("zbax", 2) << endl;
}