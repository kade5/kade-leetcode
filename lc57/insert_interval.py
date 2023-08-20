class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        new_intervals = []
        start = 0

        # find start
        pos = 0
        while pos < len(intervals):
            new_intervals.append(intervals[pos])
            if newInterval[0] >= intervals[pos][0]:
                start = pos
                break
            pos += 1

        if pos == len(intervals):
            return new_intervals.append(newInterval)

        pos += 1

        # find end
        while pos < len(intervals):
            if intervals[pos][1] > newInterval[1]:
                break
            pos += 1

        intervals[start] = [
            min(newInterval[0], intervals[start][0]),
            max(newInterval[1], intervals[pos][1]),
        ]

        for i in range(pos, len(intervals)):
            new_intervals.append(intervals[i])
        return new_intervals
