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
        if len(s1) > len(s2):
            return False
        s1_map = [0] * 26
        s2_map = [0] * 26
        s1_length = len(s1)

        for c in s1:
            s1_map[ord(c) - ord('a')] += 1
        for i in range(s1_length):
            s2_map[ord(s2[i]) - ord('a')] += 1

        if s1_map == s2_map:
            return True

        for i in range(s1_length, len(s2)):
            s2_map[ord(s2[i - s1_length]) - ord('a')] -= 1
            s2_map[ord(s2[i]) - ord('a')] += 1
            if s1_map == s2_map:
                return True

        return False


            
