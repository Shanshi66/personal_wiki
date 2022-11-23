#include<map>
#include<iostream>

using namespace std;

class Solution {
public:
    int countBalls(int lowLimit, int highLimit) {
        map<int, int> box;
        int ans = 0;
        for (int i = lowLimit; i <= highLimit; i++) {
            int tmp = 0, k = i;
            while (k > 0) {
                tmp += k%10;
                k = k/10;
            }
            if (box.find(tmp) != box.end()) {
                box[tmp] += 1;
            }
            else {
                box[tmp] = 1;
            }
            ans = max(ans, box[tmp]);
        }
        return ans;
    }
};

int main() {
    Solution test;
    int low = 1, high = 10;
    cout << test.countBalls(low, high) << endl;

    low = 5, high = 15;
    cout << test.countBalls(low, high) << endl;

    low = 19, high = 28;
    cout << test.countBalls(low, high) << endl;
}