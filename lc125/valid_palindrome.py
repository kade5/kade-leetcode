class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        """
        Given a string s, return true if it is a palindrome,
        or false otherwise.
                :type s: str
                :rtype: bool
        """
        new_string = "".join(char for char in s if char.isalnum())
        start = 0
        end = len(new_string) - 1
        while start < end:
            if new_string[start].lower() != new_string[end].lower():
                return False
            start += 1
            end -= 1
        return True
