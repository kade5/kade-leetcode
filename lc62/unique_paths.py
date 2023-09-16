class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memory = {}
        memory[(m - 1, n - 1)] = 1

        def dfs(i, j):
            nonlocal m, n
            sum1, sum2 = 0, 0
            if (i, j) in memory:
                return memory[(i, j)]

            if i < m:
                sum1 = dfs(i + 1, j)

            if j < n:
                sum2 = dfs(i, j + 1)

            memory[(i, j)] = sum1 + sum2
            return memory[(i, j)]

        return dfs(0, 0)
