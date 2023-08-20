class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        cache = [1] * len(nums)
        maximum = 1

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    cache[i] = max(cache[i], 1 + cache[j])
            maximum = max(cache[i], maximum)

        return maximum
