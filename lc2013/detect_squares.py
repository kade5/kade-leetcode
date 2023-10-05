from collections import defaultdict


class DetectSquares:
    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: list[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: list[int]) -> int:
        result = 0
        px, py = point

        for x, y in list(self.points.keys()):
            if abs(px - x) != abs(py - y) or x == px or y == py:
                continue

            result += self.points[(x, py)] * self.points[(px, y)] * self.points[(x, y)]

        return result
