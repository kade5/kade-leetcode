class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        cache = {}
        cache[(0, 0)] = 0

        def recursion(n, k):
            if (n, k) in cache:
                return cache[(n, k)]
            m = k % 2
            j = k // 2

            if (m == 0 and recursion(n - 1, j) == 0) or (
                m == 1 and recursion(n - 1, j) == 1
            ):
                cache[(n, k)] = 0
            else:
                cache[(n, k)] = 1

            return cache[(n, k)]

        return recursion(n - 1, k - 1)
