import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def distance(point: list[int]):
            return point[0] ** 2 + point[1] ** 2

        distance_list = [(distance(points[i]), i) for i in range(len(points))]
        heapq.heapify(distance_list)

        result = [points[heapq.heappop(distance_list)[1]] for _ in range(k)]
        return result
