class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        vowels = []

        for c in s:
            if c in vowel_set:
                vowels.append(c)

        vowels.sort()

        j = 0
        result = ""

        for c in s:
            if c in vowel_set:
                result += vowels[j]
                j += 1
            else:
                result += c

        return result
