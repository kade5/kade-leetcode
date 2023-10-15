from collections import defaultdict


class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        cache = defaultdict(int)
        inf = float("inf")

        def dp(i, skips):
            if (i, skips) in cache:
                return cache[(i, skips)]

            if i == len(time):
                if skips >= 0:
                    return 0
                else:
                    return inf

            if skips > len(time) - i:
                cache[(i, skips)] = 0
                return cache[(i, skips)]

            cache[(i, skips)] = min(
                dp(i + 1, skips - 1), cost[i] + dp(i + 1, skips + time[i])
            )

            return cache[(i, skips)]

        return dp(0, 0)
