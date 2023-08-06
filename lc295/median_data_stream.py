import heapq
import math


class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.middle = -math.inf
        self.nums_length = 0

    def addNum(self, num: int) -> None:
        if self.nums_length == 0:
            self.middle = num
        elif self.nums_length % 2 == 1:
            if num <= self.middle:
                heapq.heappush(self.max_heap, -num)
                heapq.heappush(self.min_heap, self.middle)
            else: # num > self.middle
                heapq.heappush(self.min_heap, num)
                heapq.heappush(self.max_heap, -self.middle)

            self.middle = -math.inf
        else:
            left = -heapq.heappop(self.max_heap)
            right = heapq.heappop(self.min_heap)

            if left < num < right:
                self.middle = num
                heapq.heappush(self.max_heap, -left)
                heapq.heappush(self.min_heap, right)
            elif num <= left:
                heapq.heappush(self.max_heap, -num)
                self.middle = left
                heapq.heappush(self.min_heap, right)
            else: # num >= right
                heapq.heappush(self.min_heap, num)
                self.middle = right
                heapq.heappush(self.max_heap, -left)

        self.nums_length += 1

    def findMedian(self) -> float:
        if self.nums_length % 2 == 1:
            return self.middle
        else: #self.nums_length % 2 == 0
            return (-self.max_heap[0] + self.min_heap[0]) / 2
