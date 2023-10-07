class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        result = []
        intervals.sort()

        def mergeIntervals(i1, i2):
            return [min(i1[0], i2[0]), max(i1[1], i2[1])]

        for r in range(len(intervals)):
            cs, _ = intervals[r]
            result.append(intervals[r])
            for i in range(len(result) - 2, -1, -1):
                _, pe = result[i]
                if cs >= pe:
                    result[i] = mergeIntervals(intervals[r], result[i])
                    result.pop()
                    break

        return len(result)
