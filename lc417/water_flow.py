class Land():
    def __init__(self, height = 0):
        self.border_po = False
        self.border_ao = False
        self.height = height
        self.lower_edges = []

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        result = []
        m = len(heights)
        n = len(heights[0])
        graph = self.buildGraph(heights)

        for r in range(m):
            for c in range(n):
                visited = set()
                stack = []
                reach_po = graph[r][c].border_po
                reach_ao = graph[r][c].border_ao
                stack.append(graph[r][c])
                visited.add(graph[r][c])

                while stack and (not reach_po or not reach_ao):
                    cur_pos = stack.pop()

                    for adj in cur_pos.lower_edges:
                        if adj not in visited:
                            if adj.border_po:
                                reach_po = True
                            if adj.border_ao:
                                reach_ao = True
                            visited.add(adj)
                            stack.append(adj)

                if reach_po and reach_ao:
                    result.append([r, c])

        return result





    def buildGraph(self, heights):
        m = len(heights)
        n = len(heights[0])

        graph = [[Land() for _ in range(n)] for _ in range(m)]

        for r in range(m):
            for c in range(n):
                land = graph[r][c]
                land.height = heights[r][c]
                if r == 0 or c == 0:
                    land.border_po = True
                if r == m - 1 or c == n - 1:
                    land.border_ao = True

                if r - 1 >= 0 and land.height >= heights[r - 1][c]:
                    land.lower_edges.append(graph[r - 1][c])
                if r + 1 < m and land.height >= heights[r + 1][c]:
                    land.lower_edges.append(graph[r + 1][c])
                if c + 1 < n and land.height >= heights[r][c + 1]:
                    land.lower_edges.append(graph[r][c + 1])
                if c - 1 >= 0 and land.height >= heights[r][c - 1]:
                    land.lower_edges.append(graph[r][c - 1])

        return graph
