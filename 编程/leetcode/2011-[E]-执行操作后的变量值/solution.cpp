#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int x = 0;
        for (const auto& str: operations) {
            if (str == "X++" || str == "++X") x++;
            else x--;
        }
        return x;
    }
};