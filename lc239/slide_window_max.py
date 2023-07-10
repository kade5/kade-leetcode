import collections


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        You are given an array of integers nums, there is a sliding window
        of size k which is moving from the very left of the array to the
        very right. You can only see the k numbers in the window. Each time
        the sliding window moves right by one position.

        Return the max sliding window for each window.
                :type nums: List[int]
                :type k: int
                :rtype: List[int]
        """
        max_index_queue = collections.deque()
        left = 0
        max_array = []

        for right in range(len(nums)):
            while max_index_queue and nums[right] >= nums[max_index_queue[-1]]:
                max_index_queue.pop()
            max_index_queue.append(right)

            if right - left + 1 >= k:
                max_array.append(nums[max_index_queue[0]])
                if left == max_index_queue[0]:
                    max_index_queue.popleft()
                left += 1

        return max_array
