class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        cache = {}

        def dfs(s1p, s2p):
            s3p = s1p + s2p
            s1_bool, s2_bool = False, False

            if (s1p, s2p) in cache:
                return cache[(s1p, s2p)]

            if s3p >= len(s3):
                return True

            if s1p < len(s1) and s3[s3p] == s1[s1p]:
                s1_bool = dfs(s1p + 1, s2p)

            if s2p < len(s2) and s3[s3p] == s2[s2p]:
                s2_bool = dfs(s1p, s2p + 1)

            cache[(s1p, s2p)] = s1_bool or s2_bool
            return cache[(s1p, s2p)]

        return dfs(0, 0)
