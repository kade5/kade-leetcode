class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort(key=lambda x:x[0])
        current_interval = intervals[0] if len(intervals) > 0 else []

        for interval in intervals[1:]:
            if current_interval[1] <= interval[0]:
                current_interval = interval
                continue
            else:
                return False

        return True
