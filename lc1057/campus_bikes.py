import heapq


class Solution:
    def assignBikes(
        self, workers: list[list[int]], bikes: list[list[int]]
    ) -> list[int]:
        assigned_bikes = set()
        assigned_workers = set()
        result = [0] * len(workers)
        heap = []

        def manhatten(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        for i, w in enumerate(workers):
            for j, b in enumerate(bikes):
                d = manhatten(w, b)
                heapq.heappush(heap, (d, i, j))

        while heap and len(assigned_workers) < len(workers):
            d, i, j = heapq.heappop(heap)

            if i not in assigned_workers and j not in assigned_bikes:
                result[i] = j
                assigned_workers.add(i)
                assigned_bikes.add(j)

        return result
