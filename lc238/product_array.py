class Solution(object):
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Given an integer array nums, return an array answer such that answer[i]
        is equal to the product of all the elements of nums except nums[i]
                :type nums: List[int]
                :rtype: List[int]
        """
        product = 1
        solution_array = []
        for num in nums:
            solution_array.append(product)
            product *= num

        product = 1
        for i in reversed(range(len(nums))):
            solution_array[i] *= product
            product *= nums[i]

        return solution_array
            


