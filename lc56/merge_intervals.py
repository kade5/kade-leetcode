class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        current_interval = intervals[0]
        result = []

        def mergeIntervals(int1, int2):
            return [min(int1[0], int2[0]), max(int1[1], int2[1])]

        for i in range(1, len(intervals)):
            if current_interval[1] < intervals[i][0]:
                result.append(current_interval)
                current_interval = intervals[i]
            else:
                current_interval = mergeIntervals(current_interval, intervals[i])

        result.append(current_interval)
        return result
