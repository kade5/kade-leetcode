class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        power_set = []
        nums.sort()

        def backtrack(i, subset):
            if i >= len(nums):
                power_set.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return power_set


