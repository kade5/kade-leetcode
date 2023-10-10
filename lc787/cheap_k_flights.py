class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        inf = 100000
        cheapest = [inf] * n
        cheapest[src] = 0

        for _ in range(k + 1):
            tmp_cheapest = cheapest.copy()
            for s, d, p in flights:
                if cheapest[s] == inf:
                    continue
                tmp_cheapest[d] = min(tmp_cheapest[d], cheapest[s] + p)

            cheapest = tmp_cheapest.copy()

        return cheapest[dst] if cheapest[dst] != inf else -1
