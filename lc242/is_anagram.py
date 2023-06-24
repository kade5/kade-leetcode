class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if t is an anagram of s,
        and false otherwise.
                        :type s: str
                        :type t: str
                        :rtype: bool
        """
        s_dict = {}
        for character in s:
            if not s_dict.get(character):
                s_dict[character] = 1
            else:
                s_dict[character] += 1
        for character in t:
            if not s_dict.get(character):
                return False
            else:
                char_left = s_dict[character] - 1
                if char_left < 0:
                    return False
                s_dict[character] = char_left

        for key, value in s_dict.items():
            if value != 0:
                return False
        return True
