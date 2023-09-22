class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len_t = len(t)
        len_s = len(s)
        if len_t > len_s:
            return 0

        cache = [[-1] * len_t for _ in range(len_s)]

        def dfs(i, j):
            if j >= len_t:
                return 1
            if i >= len_s:
                return 0

            if cache[i][j] != -1:
                return cache[i][j]

            if s[i] == t[j]:
                cache[i][j] = dfs(i + 1, j + 1) + dfs(i + 1, j)
                return cache[i][j]
            else:
                cache[i][j] = dfs(i + 1, j)
                return cache[i][j]

        return dfs(0, 0)
