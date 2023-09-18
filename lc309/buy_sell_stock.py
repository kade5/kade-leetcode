class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        memory = {}

        def dfs(i: int, orien: int) -> int:
            if i >= len(prices):
                return 0
            if (i, orien) in memory:
                return memory[(i, orien)]

            if orien == 1:
                memory[(i, orien)] = max(orien * prices[i] + dfs(i + 2, orien * -1), dfs(i + 1, orien))
            else:
                memory[(i, orien)] = max(orien * prices[i] + dfs(i + 1, orien * -1), dfs(i + 1, orien))

            return memory[(i, orien)]

        return dfs(0, -1)
