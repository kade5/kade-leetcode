import heapq


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        intervals.sort(key=lambda x: x[0])
        result = {}
        minheap = []
        i = 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minheap, (r - l + 1, r))
                i += 1

            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)

            result[q] = minheap[0][0] if minheap else -1

        return [result[q] for q in queries]
