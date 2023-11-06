#include <queue>
class SeatManager {
public:
  std::priority_queue<int> queue;
  SeatManager(int n) {
    for (int i = 1; i <= n; i++) {
      queue.push(-i);
    }
  }

  int reserve() {
    int r = queue.top();
    queue.pop();
    return -r;
  }

  void unreserve(int seatNumber) { queue.push(-seatNumber); }
};
