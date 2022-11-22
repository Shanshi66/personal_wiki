#include <iostream>
#include <string>
#include <vector>

using namespace std;


//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    void dfs(TreeNode* root, string tmp, vector<string>& result) {
        if (tmp == "") {
            tmp += to_string(root->val);
        }
        else {
            tmp += "->";
            tmp += to_string(root->val);
        }
        if (root->left == nullptr && root->right == nullptr) {
            result.push_back(tmp);
            return;
        }
        if (root->left != nullptr) {
            dfs(root->left, tmp, result);
        } 
        if (root->right != nullptr){
            dfs(root->right, tmp, result);
        }
    }

    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> result;
        if (root == nullptr) {
            return result;
        }
        dfs(root, "", result);
        return result;
    }
};

int main() {
    Solution test;
    vector<string> res = test.binaryTreePaths(nullptr);
}