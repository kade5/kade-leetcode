class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        adjacent = [[] for _ in range(n)]
        visited = set()

        for x, y in edges:
            adjacent[x].append(y)
            adjacent[y].append(x)

        def dfs(i, parent):
            if i in visited:
                return False
            visited.add(i)

            for adj in adjacent[i]:
                if adj == parent:
                    continue
                if not dfs(adj, i):
                    return False

            return True

        return dfs(0, -1) and n == len(visited)
