#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;
class Solution {
public:
  vector<int> restoreArray(vector<vector<int>> &adjacentPairs) {
    unordered_map<int, vector<int>> tree;
    unordered_set<int> visited;
    vector<int> result;

    for (int i = 0; i < adjacentPairs.size(); i++) {
      tree[adjacentPairs[i][0]].push_back(adjacentPairs[i][1]);
      tree[adjacentPairs[i][1]].push_back(adjacentPairs[i][0]);
    }

    for (auto pair : tree) {
      if (tree[pair.first].size() == 1) {
	result.push_back(pair.first);
	visited.insert(pair.first);
	break;
      }
    }

    while (visited.size() != adjacentPairs.size() + 1) {
      for (auto x : tree[result.back()]) {
	if (visited.count(x) == 0) {
	  visited.insert(x);
	  result.push_back(x);
	}
      }
    }

    return result;
  }
};
