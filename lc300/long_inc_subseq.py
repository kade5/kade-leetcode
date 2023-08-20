class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        cache = {len(nums) - 1: 1}

        def search(pos):
            if pos in cache:
                return cache[pos]
            i = pos

            while i + 1 < len(nums) and nums[i + 1] <= nums[pos]:
                i += 1

            if i + 1 < len(nums):
                cache[pos] = 1 + search(i + 1)
                return cache[pos]

            cache[pos] = 1
            return cache[pos]

        for i in range(len(nums) - 1, -1, -1):
            search(i)

        return max(cache.values())
