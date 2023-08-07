from collections import deque


class Vertex:
    def __init__(self):
        self.is_land = False
        self.edges = []


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0
        visited = set()
        grid_graph = self.buildGraph(grid)
        queue = deque()

        for r in range(len(grid_graph)):
            for c in range(len(grid_graph[0])):
                if grid_graph[r][c].is_land and grid_graph[r][c] not in visited:
                    area = 1
                    queue.append(grid_graph[r][c])
                    visited.add(grid_graph[r][c])

                    while queue:
                        current_pos = queue.popleft()

                        for adj in current_pos.edges:
                            if adj not in visited:
                                visited.add(adj)
                                queue.append(adj)
                                area += 1

                    max_area = max(max_area, area)

        return max_area

    def buildGraph(self, grid):
        m = len(grid)
        n = len(grid[0])
        vertex_grid = [[Vertex() for _ in range(n)] for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    vertex_grid[r][c].is_land = True
                    if r - 1 >= 0 and grid[r - 1][c] == 1:
                        vertex_grid[r][c].edges.append(vertex_grid[r - 1][c])
                    if r + 1 < m and grid[r + 1][c] == 1:
                        vertex_grid[r][c].edges.append(vertex_grid[r + 1][c])
                    if c - 1 >= 0 and grid[r][c - 1] == 1:
                        vertex_grid[r][c].edges.append(vertex_grid[r][c - 1])
                    if c + 1 < n and grid[r][c + 1] == 1:
                        vertex_grid[r][c].edges.append(vertex_grid[r][c + 1])

        return vertex_grid
