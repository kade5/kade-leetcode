class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = set()
        cache = set()

        def addToResult(s, l, r):
            i = l + 1
            while i < r:
                result.add(s[l] + s[i] + s[r])
                i += 1

        def countPalin(s, l, r):
            if l >= r:
                return

            if s[l] == s[r] and (l, r) not in cache:
                addToResult(s, l, r)
                cache.add((l, r))
                countPalin(s, l + 1, r - 1)
            else:
                countPalin(s, l + 1, r)
                countPalin(s, l, r - 1)

        countPalin(s, 0, len(s) - 1)
        return len(result)
