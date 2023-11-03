#import <string>
#import <vector>

using namespace std;

class Solution {
public:
  vector<string> buildArray(vector<int> &target, int n) {
    vector<string> result;
    int index = 0;

    for (int num : target) {
      while (index < num - 1) {
        result.push_back("Push");
        result.push_back("Pop");
        index++;
      }

      result.push_back("Push");
      index++;
    }

    return result;
  }
};
