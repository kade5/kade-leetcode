class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        result = 0
        intervals.sort(key=lambda x: x[0])
        current_interval = intervals[0]

        for interval in intervals[1:]:
            if current_interval[1] <= interval[0]:
                current_interval = interval
            else:
                result += 1
                current_interval = min(current_interval, interval, key=lambda x: x[1])

        return result
