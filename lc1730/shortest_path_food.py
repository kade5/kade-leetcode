from collections import deque


class Solution:
    def getFood(self, grid: list[list[str]]) -> int:
        person = (0, 0)
        food_list = []
        m = len(grid)
        n = len(grid[0])
        solution_grid = [[m * n for _ in range(n)] for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for (i, row) in enumerate(grid):
            for (j, c) in enumerate(row):
                if c == '*':
                    person = (i, j)
                elif c == '#':
                    food_list.append((i, j))

        for food in food_list:
            visited = set()
            qu = deque()
            qu.append((food, 0))
            while qu:
                pos, steps = qu.popleft()
                visited.add(pos)
                if solution_grid[pos[0]][pos[1]] > steps:
                    solution_grid[pos[0]][pos[1]] = steps
                for direct in directions:
                    if (0 <= pos[0] + direct[0] < m
                        and 0 <= pos[1] + direct[1] < n
                        and (pos[0] + direct[0], pos[1] + direct[1]) not in visited
                        and grid[pos[0] + direct[0]][pos[1] + direct[1]] != 'X'
                        and grid[pos[0] + direct[0]][pos[1] + direct[1]] != '#')\
                        and solution_grid[pos[0] + direct[0]][pos[1] + direct[1]] > steps + 1:
                        qu.append(((pos[0] + direct[0], pos[1] + direct[1]), steps + 1))

        if solution_grid[person[0]][person[1]] < m * n:
            return solution_grid[person[0]][person[1]]

        return -1
