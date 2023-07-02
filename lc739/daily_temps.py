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

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_value, stack_index = stack.pop()
                result[stack_index] = i - stack_index
            stack.append((temp, i))

        return result
