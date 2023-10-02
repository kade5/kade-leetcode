class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits) - 1

        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1

        if i < 0:
            digits[0] = 1
            digits.append(0)
        else:
            digits[i] += 1

        return digits
