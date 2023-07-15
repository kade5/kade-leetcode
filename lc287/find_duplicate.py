class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        sum_nums = -(len(nums) * (len(nums) - 1)) // 2

        for num in nums:
            sum_nums += num

        return sum_nums
