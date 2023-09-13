import heapq
import collections


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        node_hash = collections.defaultdict(list)
        visited = set()
        queue = []
        heapq.heappush(queue, [0, k])
        result = 0

        for u, v, w in times:  # u -> v with time w
            node_hash[u].append([w, v])

        while queue:
            signal, cur = heapq.heappop(queue)
            if cur in visited:
                continue
            visited.add(cur)
            result = max(result, signal)
            for adj_sig, adj in node_hash[cur]:
                if adj not in visited:
                    heapq.heappush(queue, [adj_sig + signal, adj])

        return result if len(visited) == n else -1
