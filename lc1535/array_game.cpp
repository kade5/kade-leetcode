#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {

public:
  int getWinner(vector<int> &arr, int k) {
    unordered_map<int, int> wins(arr.size());
    int max_element = arr[0];
    k = min(k, int(arr.size()));

    for (int i = 1; i < arr.size(); i++) {
      max_element = max(max_element, arr[i]);
    }

    while (wins[arr[0]] < k) {
      if (arr[0] > arr[1]) {
        arr.push_back(arr[1]);
        arr.erase(arr.begin() + 1);
      } else {
        arr.push_back(arr[0]);
        arr.erase(arr.begin());
      }
      if (arr[0] == max_element) {
	return max_element;
      }
      wins[arr[0]] += 1;
    }

    return arr[0];
  }
};
