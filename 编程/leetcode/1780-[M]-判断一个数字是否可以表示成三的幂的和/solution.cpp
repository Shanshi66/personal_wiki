#include <vector>
#include <iostream>

using namespace std;

// 思路：三进制

class Solution {
public:
    bool checkPowersOfThree(int n) {
        while (n > 0) {
            if (n % 3 > 1) {
                return false;
            }
            n = n/3;
        }
        return true;
    }
};