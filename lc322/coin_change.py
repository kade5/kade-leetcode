class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        coins.sort()
        memory = {0: 0}
        maximum = amount + 1

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    memory[i] = min(
                        memory.get(i, maximum), 1 + memory.get(i - coin, maximum)
                    )

        return memory.get(amount, maximum) if memory.get(amount, maximum) < maximum else -1
