#include <algorithm>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {

public:
  int getWinner(vector<int> &arr, int k) {
    queue<int> game;
    int max_element = arr[0];
    int current = arr[0];
    int wins = 0;

    for (int i = 1; i < arr.size(); i++) {
      max_element = max(max_element, arr[i]);
      game.push(arr[i]);
    }

    while (!game.empty()) {
      auto value = game.front();
      game.pop();

      if (current > value) {
        game.push(value);
        wins += 1;
      } else {
        game.push(current);
        current = value;
        wins = 1;
      }

      if (current == max_element || wins == k) {
        return current;
      }
    }

    return current;
  }
};
