from collections import defaultdict, deque
from math import sqrt


class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        tree = defaultdict(list)

        for i0, (x0, y0, r0) in enumerate(bombs):
            for i, (x, y, _) in enumerate(bombs):
                d = sqrt((x - x0) ** 2 + (y - y0) ** 2)
                if d <= r0:
                    tree[i0].append(i)

        def bfs(i, tree) -> int:
            queue = deque()
            result = 0
            exploded = set()

            queue.append(i)

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
        for i, _ in enumerate(bombs):
            result = max(result, bfs(i, tree))

        return result
