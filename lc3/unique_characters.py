class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring without
        repeating characters.
                :type s: str
                :rtype: int
        """
        current_sub_length = 0
        max_sub_length = 0
        char_map = {}

        for i, l in enumerate(s):
            if char_map.get(l) is None or char_map.get(l) < i - current_sub_length:
                current_sub_length += 1
                char_map[l] = i
            else:
                current_sub_length = current_sub_length - (
                    char_map.get(l) - (i - current_sub_length)
                )
                char_map[l] = i
            max_sub_length = max(max_sub_length, current_sub_length)

        return max_sub_length
