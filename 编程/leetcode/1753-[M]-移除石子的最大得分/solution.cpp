#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int maximumScore(int a, int b, int c) {
        if (c < b) swap(b, c);
        if (c < a) swap(a, c);
        if (b < a) swap(a, b);
        int score = 0;
        if (c-b > a) {
            score = a+b;
        }
        else {
            score += c-b;
            a = a-(c-b);
            score += a;
            score += b-(a+1)/2;
        }
        return score;
    }
};

int main() {
    Solution test;
    cout << test.maximumScore(2, 4, 6) << endl;
    cout << test.maximumScore(4, 4, 6) << endl;
    cout << test.maximumScore(1, 8, 8) << endl;
    cout << test.maximumScore(5, 10, 12) << endl;
}