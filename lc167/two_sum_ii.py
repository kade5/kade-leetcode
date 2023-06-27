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
        for index in range(len(numbers)):
            index2 = index + 1
            target_num = target - numbers[index]
            while index2 < len(numbers):
                if numbers[index2] == target_num:
                    return [index + 1, index2 + 1]
                elif numbers[index2] > target_num:
                    break
                index2 += 1

        return []
