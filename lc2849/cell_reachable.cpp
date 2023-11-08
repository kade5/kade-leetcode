#include <algorithm>
#include <cstdlib>
class Solution {
public:
  bool isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
    int width = abs(sx - fx);
    int height = abs(sy - fy);

    int min_time = abs(sx - fx) + abs(sy - fy);

    if (sx == fx && sy == fy and t == 1) {
      return false;
    }

    return t >= std::max(width, height);
  }
};
