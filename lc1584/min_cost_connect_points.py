import heapq


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        visit = set()
        cost = 0
        adj = {i: [] for i in range(len(points))}
        minheap = [[0, 0]]

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        while len(visit) < len(points):
            c, i = heapq.heappop(minheap)
            if i in visit:
                continue

            cost += c
            visit.add(i)

            for ac, a in adj[i]:
                if a not in visit:
                    heapq.heappush(minheap, [ac, a])

        return cost
