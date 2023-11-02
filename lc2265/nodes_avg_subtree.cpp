#include <cstddef>
#include <utility>
// Definition for a binary tree node.
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
public:
  int result = 0;
  int averageOfSubtree(TreeNode *root) {
    dfs(root);
    return result;
  }
  std::pair<int, int> dfs(TreeNode *node) {
    if (node == NULL) {
      return {0, 0};
    }
    int sum = node->val;
    int count = 1;
    std::pair<int, int> left = dfs(node->left);
    std::pair<int, int> right = dfs(node->right);
    sum = sum + left.first + right.first;
    count = count + left.second + right.second;

    if (sum / count == node->val) {
      result += 1;
    }

    return {sum, count};
  }
};
