class Solution(object):
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        Given a 1-indexed array of integers numbers that is already sorted in
        non-decreasing order, find two numbers such that they add up to a
        specific target number.
        Return the indices of the two numbers, index1 and index2, added by one
        as an integer array [index1, index2] of length 2.
                :type numbers: List[int]
                :type target: int
                :rtype: List[int]
        """
        index1 = 0
        index2 = len(numbers) - 1

        while index1 < index2:
            current_sum = numbers[index1] + numbers[index2]
            if current_sum == target:
                return [index1 + 1, index2 + 1]
            elif current_sum > target:
                index2 -= 1
            else:
                index1 += 1

        return []
