class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        value = pref[0]
        result = [value]

        for i in range(1, len(pref)):
            result.append(value ^ pref[i])
            value = pref[i]

        return result
