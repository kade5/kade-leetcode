class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        moves = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]
        current = set()
        next = set()
        current.add((fx, fy))

        for _ in range(1, t + 1):
            for x, y in current:
                for x0, y0 in moves:
                    if x + x0 >= 1 and y + y0 >= 1:
                        next.add((x + x0, y + y0))

            current = next
            next = set()

        return (sx, sy) in current
