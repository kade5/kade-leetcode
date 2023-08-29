class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = sum(nums)
        current_sum = 0

        for rp in range(len(nums)):
            current_sum += nums[rp]
            max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
                

        return max_sum
