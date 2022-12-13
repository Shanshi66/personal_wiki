#include <string>
#include <set>

using namespace std;


class Solution {
public:
    bool checkIfPangram(string sentence) {
        set<char> char_set;
        for (auto& c: sentence) {
            char_set.insert(c);
        }
        if (char_set.size() == 26) {
            return true;
        }
        return false;
    }
};