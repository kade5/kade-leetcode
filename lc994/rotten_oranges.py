from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        num_fresh = 0
        queue = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        time_rotten = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    num_fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))


        while queue and num_fresh > 0:

            for _ in range(len(queue)):
                x, y = queue.popleft()

                for x0, y0 in directions:
                    if x + x0 < 0 or x + x0 >= ROWS or y + y0 < 0 or y + y0 >= COLS:
                        continue
                    if grid[x + x0][y + y0] == 1:
                        grid[x + x0][y + y0] = 2
                        queue.append((x + x0, y + y0))
                        num_fresh -= 1

            time_rotten += 1

        if num_fresh > 0:
            return -1
        
        return time_rotten
