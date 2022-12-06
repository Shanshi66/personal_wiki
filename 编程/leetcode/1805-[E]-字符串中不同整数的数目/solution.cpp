#include<string>
#include<iostream>
#include<set>
#include<unordered_set>

using namespace std;

class Solution {
public:
    bool is_digit(char c) {
        if (c >= '0' && c <= '9') return true;
        return false;
    }

    int numDifferentIntegers(string word) {
        int n = word.length(), i = 0;
        unordered_set<string> nums;
        while (i < n) {
            if (!is_digit(word[i])) {
                i++;
                continue;
            }
            int j = i;
            while (j < n && word[j] == '0') j++;
            if (j < n && is_digit(word[j])) {
                int k = j+1;
                while (k < n && is_digit(word[k])) k++;
                nums.insert(string(word.begin()+j, word.begin()+k));
                i = k;
            } 
            else {
                nums.insert("0");
                i = j+1;
            }
            
        }
        return nums.size();
    }
};