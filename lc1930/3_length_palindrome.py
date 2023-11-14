class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        result = 0

        for letter in letters:
            i = -1
            j = -1

            for pos, c in enumerate(s):
                if c == letter:
                    if i == -1:
                        i = pos
                    else:
                        j = pos

            palin = set()
            for pos in range(i + 1, j):
                palin.add(s[pos])

            result += len(palin)

        return result
