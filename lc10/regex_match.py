class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        m = len(s)
        n = len(p)

        def dfs(i, j):
            if i >= m and j >= n:
                return True
            if j >= n:
                return False

            next_char = p[j + 1] if j + 1 < n else "#"

            if i >= m and next_char == "*":
                return dfs(i, j + 2)

            if i >= m:
                return False

            if (i, j) in cache:
                return cache[(i, j)]

            if next_char == "*":
                if s[i] != p[j] and p[j] != ".":
                    cache[(i, j)] = dfs(i, j + 2)
                else:
                    cache[(i, j)] = dfs(i + 1, j) or dfs(i, j + 2)

            else:
                if s[i] != p[j] and p[j] != ".":
                    cache[(i, j)] = False
                else:
                    cache[(i, j)] = dfs(i + 1, j + 1)

            return cache[(i, j)]

        return dfs(0, 0)
