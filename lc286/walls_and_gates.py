from collections import deque


class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()
        ROWS = len(rooms)
        COLS = len(rooms[0])
        distance = 1
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for r0, c0 in directions:
                    if (
                        r + r0 < 0
                        or r + r0 >= ROWS
                        or c + c0 < 0
                        or c + c0 >= COLS
                        or rooms[r + r0][c + c0] <= distance
                    ):
                        continue

                    rooms[r + r0][c + c0] = distance
                    queue.append((r + r0, c + c0))

            distance += 1
