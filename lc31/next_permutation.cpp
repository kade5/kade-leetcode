#include <vector>

using namespace std;
class Solution {
public:
  void nextPermutation(vector<int> &nums) {
    int rp = nums.size() - 1;
    int lp = 0;

    for (auto i = rp - 1; i >= 0; i--) {
      if (nums[i] < nums[i + 1]) {
        lp = i;
        break;
      }
    }

    for (auto i = rp; i > lp; i--) {
      if (nums[i] > nums[lp]) {
        swap(nums, i, lp);
	lp++;
        break;
      }
    }
    while (lp < rp) {
      swap(nums, lp, rp);
      lp++;
      rp--;
    }
  }

  void swap(vector<int> &nums, int a, int b) {
    int tmp = nums[a];
    nums[a] = nums[b];
    nums[b] = tmp;
  }
};
