#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    unordered_map<int, int> target_map;
    vector<int> result;

    for (int i = 0; i < nums.size(); i++) {
      int pair = target - nums[i];
      target_map[pair] = i;
    }

    for (int i = 0; i < nums.size(); i++) {
      if (target_map.count(nums[i]) && target_map[nums[i]] != i) {
        result = {i, target_map[nums[i]]};
        break;
      }
    }
    return result;
  }
};
