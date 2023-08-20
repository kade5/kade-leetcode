class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        cache = {len(nums) - 1: 1}

        for i in range(len(nums) - 2, -1, -1):
            maximum = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    maximum = max(maximum, 1 + cache[j])
                cache[i] = maximum

        return max(cache.values())
