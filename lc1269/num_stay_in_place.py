class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        base = 10**9 + 7
        cache = {}
        cache[(0, 0)] = 1

        def dp(i, steps):
            if (i, steps) in cache:
                return cache[(i, steps)]

            if i >= arrLen or i < 0 or steps <= 0:
                return 0

            cache[(i, steps)] = (
                dp(i, steps - 1) + dp(i - 1, steps - 1) + dp(i + 1, steps - 1)
            ) % base

            return cache[(i, steps)]

        return dp(0, steps)
