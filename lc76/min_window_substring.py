import math


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Given two strings s and t of lengths m and n respectively, return the minimum window
        substring
        of s such that every character in t (including duplicates) is included
        in the window. If there is no such substring, return the empty string "".

        The testcases will be generated such that the answer is unique.
                :type s: str
                :type t: str
                :rtype: str
        """
        if len(t) > len(s):
            return ""

        t_map = {}
        window_map = {}
        have = 0

        for c in t:
            t_map[c] = t_map.get(c, 0) + 1

        need = len(t_map)
        min_window = (math.inf, -1, -1)
        left = 0

        for right, c in enumerate(s):
            if t_map.get(c):
                window_map[c] = window_map.get(c, 0) + 1
                if window_map.get(c) == t_map.get(c):
                    have += 1

            while have == need:
                min_window = min(
                    min_window, (right - left + 1, left, right), key=lambda x: x[0]
                )
                if left == right:
                    break
                if window_map.get(s[left]):
                    window_map[s[left]] = window_map.get(s[left]) - 1
                    if window_map[s[left]] < t_map[s[left]]:
                        have -= 1
                left += 1

        if min_window[1] == -1:
            return ""

        return s[min_window[1] : min_window[2] + 1]
