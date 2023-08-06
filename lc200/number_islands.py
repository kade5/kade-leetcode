from collections import deque


class Vertex:
    def __init__(self):
        self.is_land = False
        self.edges = []


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0
        visited = set()
        vertex_grid = self.buildGraph(grid)
        m = len(grid)
        n = len(grid[0])

        for r in range(m):
            for c in range(n):
                if vertex_grid[r][c].is_land and vertex_grid[r][c] not in visited:
                    queue = deque()
                    visited.add(vertex_grid[r][c])
                    queue.append(vertex_grid[r][c])

                    while queue:
                        vertex = queue.popleft()
                        for adj in vertex.edges:
                            if adj not in visited:
                                visited.add(adj)
                                queue.append(adj)
                    islands += 1

        return islands

    def buildGraph(self, grid):
        m = len(grid)
        n = len(grid[0])
        vertex_grid = [[Vertex() for _ in range(n)] for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    vertex_grid[r][c].is_land = True
                    if r - 1 >= 0 and grid[r - 1][c] == "1":
                        vertex_grid[r][c].edges.append(vertex_grid[r - 1][c])
                    if r + 1 < m and grid[r + 1][c] == "1":
                        vertex_grid[r][c].edges.append(vertex_grid[r + 1][c])
                    if c - 1 >= 0 and grid[r][c - 1] == "1":
                        vertex_grid[r][c].edges.append(vertex_grid[r][c - 1])
                    if c + 1 < n and grid[r][c + 1] == "1":
                        vertex_grid[r][c].edges.append(vertex_grid[r][c + 1])

        return vertex_grid
