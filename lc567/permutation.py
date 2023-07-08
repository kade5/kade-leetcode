from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Given two strings s1 and s2, return true if s2 contains a
        permutation of s1, or false otherwise.

        In other words, return true if one of s1's permutations is the
        substring of s2.
                :type s1: str
                :type s2: str
                :rtype: bool
        """
        char_map = defaultdict(int)

        for c in s1:
            char_map[c] = char_map.get(c, 0) + 1

        left = 0
        right = 0

        while right < len(s2):
            test_map = char_map.copy()
            s1_len = len(s1)
            if char_map.get(s2[left]) is None:
                left += 1
                right = left
            else:
                while right < len(s2) and test_map.get(s2[right]) and s1_len > 0:
                    test_map[s2[right]] = test_map.get(s2[right]) - 1
                    s1_len -= 1
                    right += 1
                if s1_len == 0:
                    return True
                if right < len(s2) and char_map.get(s2[right]) is None:
                    left = right
                    right = left
                    continue
                left += 1
                right = left

        return False
