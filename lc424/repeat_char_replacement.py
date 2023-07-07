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
        char_set = set(c for c in s)

        for replace in char_set:
            current_longest = 0
            used_replacements = 0
            for i, c in enumerate(s):
                if c == replace:
                    current_longest += 1
                else:
                    if used_replacements < k:
                        used_replacements += 1
                        current_longest += 1
                    else:
                       for check in s[i - current_longest:i]:
                            if check != replace:
                                break
                            current_longest -= 1
                longest_substring = max(longest_substring, current_longest)

        return longest_substring
