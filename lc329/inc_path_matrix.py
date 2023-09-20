class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        sorted_matrix = [[matrix[i][j], i, j] for i in range(m) for j in range(n)]
        sorted_matrix.sort()
        cache = [[0] * n for _ in range(m)]
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        result = 1

        for val, i, j in sorted_matrix:
            current_max = 1
            for x, y in direction:
                if (
                    i + x < m
                    and i + x >= 0
                    and j + y < n
                    and j + y >= 0
                    and val > matrix[i + x][j + y]
                ):
                    current_max = max(current_max, cache[i + x][j + y] + 1)

            result = max(result, current_max)
            cache[i][j] = current_max
        return result

