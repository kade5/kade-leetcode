from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.time_map = defaultdict(list)
        latest_timestamp = 0
        """can be used to make sure timestamps are always increasing
            however does not need to be implemented for this
            problem as that is already guaranteed."""

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Stores the key key with the value value at the given time timestamp.
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if self.time_map.get(key):
            self.time_map[key].append((timestamp, value))
        else:
            self.time_map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        """
        Returns a value such that set was called previously, with
        timestamp_prev <= timestamp. If there are multiple such values,
        it returns the value associated with the largest timestamp_prev.
        If there are no values, it returns "".
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        prev_value = (0, "")
        if self.time_map.get(key):
            value_list = self.time_map[key]
            left = 0
            right = len(value_list) - 1
            while left <= right:
                mid = (left + right) // 2
                if value_list[mid][0] == timestamp:
                    prev_value = (timestamp, value_list[mid][1])
                    break
                elif value_list[mid][0] > timestamp:
                    right = mid - 1
                else:
                    prev_value = max((prev_value, value_list[mid]), key=lambda x: x[0])
                    left = mid + 1
        return prev_value[1]
