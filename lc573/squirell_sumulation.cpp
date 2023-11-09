#include <cstdlib>
#include <queue>
#include <tuple>

using namespace std;
class Solution {
public:
  int minDistance(int height, int width, vector<int> &tree,
                  vector<int> &squirrel, vector<vector<int>> &nuts) {
    priority_queue<tuple<int, int>, vector<tuple<int, int>>,
                   greater<tuple<int, int>>>
        tree_dist;
    priority_queue<tuple<int, int>, vector<tuple<int, int>>,
                   greater<tuple<int, int>>>
        sq_dist;
    int result = 0;

    for (int i = 0; i < nuts.size(); i++) {
      tuple<int, int> ds = {
          abs(nuts[i][0] - squirrel[0]) + abs(nuts[i][1] - squirrel[1]), i};
      tuple<int, int> dt = {
          abs(nuts[i][0] - tree[0]) + abs(nuts[i][1] - tree[1]), i};

      sq_dist.push(ds);
      tree_dist.push(dt);
    }

    tuple<int, int> first = sq_dist.top();
    result += get<0>(first);
    int index = get<1>(first);
    result += (abs(nuts[index][0] - tree[0]) + abs(nuts[index][1] - tree[1]));

    while (!tree_dist.empty()) {
      tuple<int, int> nut = tree_dist.top();
      tree_dist.pop();

      if (get<1>(nut) != index) {
        result += (2 * get<0>(nut));
      }
    }

    return result;
  }
};
