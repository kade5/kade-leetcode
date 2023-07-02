class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        Given an array of integers temperatures represents the daily
        temperatures, return an array answer such that answer[i] is the
        number of days you have to wait after the ith day to get a warmer
        temperature. If there is no future day for which this is possible,
        keep answer[i] == 0 instead.
                :type temperatures: List[int]
                :rtype: List[int]
        """
        stack = []
        result = [0] * len(temperatures)
        largest_temp = 0

        for i, temp in reversed(list(enumerate(temperatures))):
            if temp > largest_temp:
                largest_temp = temp
                stack = [largest_temp]
                continue
            else:
                for j, s_value in reversed(list(enumerate(stack))):
                    if s_value > temp:
                        result[i] += len(stack) - j
                        break
                stack.append(temp)

        return result
