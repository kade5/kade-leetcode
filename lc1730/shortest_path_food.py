from collections import deque


class Solution:
    def getFood(self, grid: list[list[str]]) -> int:
        person = (0, 0)
        m = len(grid)
        n = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for (i, row) in enumerate(grid):
            for (j, c) in enumerate(row):
                if c == '*':
                    person = (i, j)
                    break

        visited = set()
        qu = deque()
        qu.append((person, 0))
        visited.add(person)
        while qu:
            pos, steps = qu.popleft()
            if grid[pos[0]][pos[1]] == '#':
                return steps
            for direct in directions:
                if (0 <= pos[0] + direct[0] < m
                    and 0 <= pos[1] + direct[1] < n
                    and (pos[0] + direct[0], pos[1] + direct[1]) not in visited
                    and grid[pos[0] + direct[0]][pos[1] + direct[1]] != 'X'):
                    qu.append(((pos[0] + direct[0], pos[1] + direct[1]), steps + 1))
                    visited.add((pos[0] + direct[0], pos[1] + direct[1]))

        return -1
