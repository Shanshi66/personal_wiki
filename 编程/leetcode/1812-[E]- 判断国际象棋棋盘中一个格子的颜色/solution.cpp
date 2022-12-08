#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    bool squareIsWhite(string coordinates) {
        if (((coordinates[0]-'a'+1)&1) == ((coordinates[1]-'1'+1)&1)) {
            return false;
        }
        return true;
    }
};

int main() {
    Solution test;
    cout << test.squareIsWhite("a1") << endl;
    cout << test.squareIsWhite("h3") << endl;
    cout << test.squareIsWhite("c7") << endl;
}