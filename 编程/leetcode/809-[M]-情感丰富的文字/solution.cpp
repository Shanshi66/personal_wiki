#include<string>
#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    int expressiveWords(string s, vector<string>& words) {
        int num_words = words.size(), m = s.size();
        vector<int> ptr(num_words, 0);
        int i = 0;

        while (i < m) {
            int cnt = 1, j = i;

            while (j+1 < m && s[j] == s[j+1]) {
                cnt++;
                j++;
            }
            
            for (int k = 0; k < num_words; k++) {
                int tmp_cnt = 1, t = ptr[k];
                if (ptr[k] == -1) {
                    continue;
                }
                if (words[k][t] != s[i]) {
                    ptr[k] = -1;
                    continue;
                }
                while (t+1 < words[k].size() && words[k][t] == words[k][t+1]) {
                    tmp_cnt++;
                    t++;
                }
                if (tmp_cnt < cnt && cnt >= 3 or tmp_cnt == cnt) {
                    ptr[k] = t+1;
                }
                else {
                    ptr[k] = -1;
                }
            }
            i = j+1;
        }
        int res = 0;
        for (int j = 0; j < num_words; j++) {
            if (ptr[j] == words[j].size()) res++;
        }
        return res;
    }
};



