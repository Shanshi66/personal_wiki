#include <string>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    string largestMerge(string word1, string word2) {
        int n = word1.size(), m = word2.size();
        string merge;
        int i = 0, j = 0;
        while (i < n && j < m) {
            if (word1[i] < word2[j]) {
                merge += word2[j++];
            }
            else if (word1[i] > word2[j]) {
                merge += word1[i++];
            }
            else {
                int t = i+1, s = j+1;
                while (t < n && s < m && word1[t] == word2[s]){
                    t++;
                    s++;
                }
                if (t == n) {
                    merge += word2[j++];
                }
                else if (s == m) {
                    merge += word1[i++];
                }
                else if (word1[t] > word2[s]) {
                    merge += word1[i++];
                }
                else {
                    merge += word2[j++];
                }
            }
        }
        if (i < n) {
            merge.insert(merge.end(), word1.begin()+i, word1.end());
        }
        if (j < m) {
            merge.insert(merge.end(), word2.begin()+j, word2.end());
        }
        return merge;
    }
};

int main() {
    Solution test;
    cout << test.largestMerge("cabaa", "bcaaa") << endl;
    cout << test.largestMerge("abcabc", "abdcaba") << endl;
}