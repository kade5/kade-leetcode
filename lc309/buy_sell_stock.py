class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        memory = {}

        def dfs(i: int, orien: int) -> int:
            if i >= len(prices):
                return 0
            if i in memory:
                return memory[i]

            if orien == 1:
                memory[i] = max(orien * prices[i] + dfs(i + 2, orien * -1), dfs(i + 1, orien))
            else:
                memory[i] = max(orien * prices[i] + dfs(i + 1, orien * -1), dfs(i + 1, orien))

            return memory[i]

        return dfs(0, -1)
