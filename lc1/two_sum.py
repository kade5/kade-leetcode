class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.
                :type nums: List[int]
                :type target: int
                :rtype: List[int]
        """
        sum_dict = {}
        for i, num in enumerate(nums):
            sum = target - num
            if sum_dict.get(sum, -1) >= 0:
                return [sum_dict[sum], i]
            sum_dict[num] = i
        return []
