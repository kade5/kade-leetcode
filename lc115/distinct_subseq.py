class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        cache = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        for i in range(len(s) + 1):
            cache[0][i] = 1

        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                x = i - 1
                y = j - 1
                if j > i:
                    cache[i][j] = 0

                if cache[i][j - 1] == 0:
                    if t[x] == s[y]:
                        cache[i][j] = cache[i - 1][j]
                    else:
                        cache[i][j] = 0
                else:
                    current_max = max(cache[i - 1][j], cache[i][j - 1])
                    if t[x] == s[y]:
                        cache[i][j] = current_max + 1
                    else:
                        cache[i][j] = current_max

        return cache[len(t)][len(s)]
