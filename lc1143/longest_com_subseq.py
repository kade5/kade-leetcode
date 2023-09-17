class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memory = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            sub_len = 0
            if i >= m or j >= n:
                return 0
            if memory[i][j] != -1:
                return memory[i][j]

            if text1[i] == text2[j]:
                sub_len = dfs(i + 1, j + 1) + 1
            else:
                sub_len = max(dfs(i + 1, j), dfs(i, j + 1))

            memory[i][j] = sub_len
            return sub_len

        return dfs(0, 0)
