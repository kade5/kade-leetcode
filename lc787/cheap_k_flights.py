from collections import defaultdict


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        inf = 100000
        cheapest = [inf] * n
        cheapest[src] = 0
        graph = defaultdict(list)

        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))

        for _ in range(k + 1):
            for i in range(n):
                prev = cheapest[i]
                if prev == inf:
                    continue

                for d, price in graph[i]:
                    cheapest[d] = min(cheapest[d], price + prev)

        return cheapest[dst] if cheapest[dst] != inf else -1
