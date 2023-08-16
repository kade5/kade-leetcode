class Solution:
    def rob(self, nums: list[int]) -> int:
        memory: list[int]
        memory = [None] * len(nums)

        def robFrom(n):
            if n >= len(nums):
                return 0

            if memory[n] is not None:
                return memory[n]

            if n == len(nums) - 2:
                memory[n] = max(nums[n], nums[n + 1])
                return memory[n]

            memory[n] = max(nums[n] + robFrom(n + 2), robFrom(n + 1))
            return memory[n]

        return max(robFrom(0), robFrom(1))
