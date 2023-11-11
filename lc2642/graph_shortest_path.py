from collections import defaultdict
import heapq


class Graph:
    def __init__(self, n: int, edges: list[list[int]]):
        self.n = n
        self.graph = defaultdict(list)

        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: list[int]) -> None:
        self.graph[edge[0]].append((edge[2], edge[1]))

    def shortestPath(self, node1: int, node2: int) -> int:
        inf = 10**8
        min_dist = [inf] * self.n
        min_dist[node1] = 0
        pq = [(0, node1)]

        while pq:
            cur_d, cur_n = heapq.heappop(pq)

            if cur_n == node2:
                return cur_d

            for d, x in self.graph[cur_n]:
                new_d = d + cur_d

                if new_d < min_dist[x]:
                    heapq.heappush(pq, (new_d, x))
                    min_dist[x] = new_d

        return -1
