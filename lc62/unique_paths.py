class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memory = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                memory[i][j] = memory[i - 1][j] + memory[i][j - 1]

        return memory[m - 1][n - 1]

