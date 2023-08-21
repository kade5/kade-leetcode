class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        result = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval = self.mergeInterval(newInterval, intervals[i])

        result.append(newInterval)
        return result

    def mergeInterval(self, interval1, interval2):
        return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]
