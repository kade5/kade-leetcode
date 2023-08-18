class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        result_length = 0

        def checkPalindrome(l, r):
            nonlocal result_length
            nonlocal result
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > result_length:
                    result = s[l : r + 1]
                    result_length = r - l + 1

                l -= 1
                r += 1

        for i in range(len(s)):
            checkPalindrome(i, i)
            checkPalindrome(i, i + 1)

        return result
