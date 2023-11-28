class Solution:
    def knightDialer(self, n: int) -> int:
        modulo = 10**9 + 7
        m = 10
        knight_map = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [7, 1, 0],
            [6, 2],
            [1, 3],
            [2, 4],
        ]

        cache = [[1] * m for _ in range(n + 1)]

        for i in range(2, n + 1):
            for j in range(m):
                movements = 0

                for next in knight_map[j]:
                    movements = (movements + cache[i - 1][next]) % modulo

                cache[i][j] = movements

        total = 0

        for value in cache[n]:
            total = (total + value) % modulo

        return total
