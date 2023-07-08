class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        You are given a string s and an integer k. You can choose any
        character of the string and change it to any other uppercase English
        character. You can perform this operation at most k times.

        Return the length of the longest substring containing the same letter
        you can get after performing the above operations.
                :type s: str
                :type k: int
                :rtype: int
        """
        longest_substring = 0
        char_dict = {}
        right = 0
        left = 0

        while right < len(s):
            char_dict[s[right]] = char_dict.get(s[right], 0) + 1
            while right - left + 1 - max(char_dict.values()) > k:
                char_dict[s[left]] = char_dict.get(s[left]) - 1
                left += 1
            longest_substring = max(longest_substring, right - left + 1)
            right += 1

        return longest_substring
