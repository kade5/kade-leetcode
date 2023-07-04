class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Given an array of integers nums which is sorted in ascending order,
        and an integer target, write a function to search target in nums.
        If target exists, then return its index. Otherwise, return -1.
                :type nums: List[int]
                :type target: int
                :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            index = (end + start) // 2
            if nums[index] == target:
                return index
            elif target > nums[index]:
                start = index + 1
            else:
                end = index - 1

        return -1
