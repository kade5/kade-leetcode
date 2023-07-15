class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow_pointer = 0
        fast_pointer = 0

        while True:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[nums[fast_pointer]]
            if slow_pointer == fast_pointer:
                break

        start_pointer = 0
        while slow_pointer != start_pointer:
            slow_pointer = nums[slow_pointer]
            start_pointer = nums[start_pointer]

        return start_pointer

