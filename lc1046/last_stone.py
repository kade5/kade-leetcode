import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-x for x in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if y - x != 0:
                heapq.heappush(stones, y - x)

        if len(stones) == 0:
            return 0

        return -stones[0]
