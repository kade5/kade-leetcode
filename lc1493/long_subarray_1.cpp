#include <algorithm>
#include <vector>
using namespace std;
class Solution {
public:
  int longestSubarray(vector<int> &nums) {
    int lp = 0;
    int rp = 0;
    int sk = -1;
    int longest = 0;

    while (rp < nums.size()) {
      if (nums[rp] != 1) {
        lp = sk + 1;
        sk = rp;
      }

      longest = max(rp - lp, longest);
      rp++;
    }

    return longest;
  }
};
