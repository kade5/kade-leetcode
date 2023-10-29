from collections import defaultdict, deque
from math import sqrt


class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        tree = defaultdict(list)

        for x0, y0, r0 in bombs:
            for x, y, _ in bombs:
                d = sqrt((x - x0) ** 2 + (y - y0) ** 2)
                if d <= r0:
                    tree[(x0, y0)].append((x, y))

        def bfs(x, y, tree) -> int:
            queue = deque()
            result = 0
            exploded = set()

            queue.append((x, y))

            while queue:
                cur = queue.popleft()
                if cur in exploded:
                    continue

                exploded.add(cur)
                result += 1

                for child in tree[cur]:
                    queue.append(child)

            return result

        result = 0
        for x, y, _ in bombs:
            result = max(result, bfs(x, y, tree))

        return result
