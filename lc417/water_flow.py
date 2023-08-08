class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        result = []
        pacific = set()
        atlantic = set()
        m = len(heights)
        n = len(heights[0])

        def dfs(r, c, visited):
            if (r, c) in visited or r >= m or c >= n or r < 0 or c < 0:
                return

            visited.add((r, c))

            if r > 0 and heights[r][c] <= heights[r - 1][c]:
                dfs(r - 1, c, visited)
            if r < m - 1 and heights[r][c] <= heights[r + 1][c]:
                dfs(r + 1, c, visited)

            if c > 0 and heights[r][c] <= heights[r][c - 1]:
                dfs(r, c - 1, visited)
            if c < n - 1 and heights[r][c] <= heights[r][c + 1]:
                dfs(r, c + 1, visited)



        for c in range(n):
            dfs(0, c, pacific)
            dfs(m - 1, c, atlantic)

        for r in range(m):
            dfs(r, 0, pacific)
            dfs(r, n - 1, atlantic)

        for r in range(m):
            for c in range(n):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result
