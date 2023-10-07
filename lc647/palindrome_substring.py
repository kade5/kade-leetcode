class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        def checkPalindrome(l, r):
            nonlocal result
            nonlocal s

            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1

                l -= 1
                r += 1

        for i in range(len(s)):
            checkPalindrome(i, i)
            checkPalindrome(i, i + 1)

        return result
