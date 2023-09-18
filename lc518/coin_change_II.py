class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        cache = set()
        coin_amount = [0 * len(coins)]
        result = 0

        def dfs(coin_amount: list[int], coin_total):
            nonlocal result
            if coin_total > amount or coin_amount in cache:
                return

            if coin_total == amount:
                result += 1
                return

            cache.add(coin_amount)

            for i in range(len(coins)):
                coin = coins[i]
                coin_amount[i] += 1
                dfs(coin_amount, coin + coin_total)

        dfs(coin_amount, 0)
        return result

        
