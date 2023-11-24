class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        l = 0
        r = len(piles) - 1
        result = 0

        while l < r:
            result += piles[r - 1]
            l += 1
            r -= 2

        return result
