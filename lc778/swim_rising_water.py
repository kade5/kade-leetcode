import heapq


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        next = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        min_heap = [[grid[0][0], (0, 0)]]
        visited = set()
        x_len = len(grid)
        y_len = len(grid[0])

        while min_heap:
            h, (x, y) = heapq.heappop(min_heap)
            if (x, y) in visited:
                continue

            visited.add((x, y))

            for x0, y0 in next:
                if (
                    (x + x0, y + y0) not in visited
                    and x + x0 >= 0
                    and x + x0 < x_len
                    and y + y0 >= 0
                    and y + y0 < y_len
                ):
                    min_path = max(h, grid[x + x0][y + y0])
                    if x + x0 == x_len - 1 and y + y0 == y_len - 1:
                        return min_path
                    heapq.heappush(min_heap, [min_path, (x + x0, y + y0)])

        return 0
