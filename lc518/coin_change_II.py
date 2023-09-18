class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        cache = [[1] * (amount + 1) for _ in range(len(coins))]

        for c in range(len(coins) - 1, -1, -1):
            for a in range(1, amount + 1):
                coin_amount = a - coins[c]
                if coin_amount < 0:
                    with_coin = 0
                else:
                    with_coin = cache[c][coin_amount]
                if c + 1 >= len(coins):
                    without_coin = 0
                else:
                    without_coin = cache[c + 1][a]
                cache[c][a] = with_coin + without_coin

        return cache[0][amount]
