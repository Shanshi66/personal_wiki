#include<string>
#include<vector>

using namespace std;


class Solution {
public:
    int secondHighest(string s) {
        char max_digit = 0, second_digit = 0;
        for (auto& c: s) {
            if (!(c >= '0' && c <= '9')) continue;
            if (c > max_digit) {
                second_digit = max_digit;
                max_digit = c;
            }
            if (c > second_digit && c < max_digit) {
                second_digit = c;
            }
        }
        
        if (second_digit > 0) 
            return second_digit-'0';
        else
            return -1;
    }
};