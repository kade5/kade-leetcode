class Solution:
    def rob(self, nums: list[int]) -> int:
        memory = {}

        def robRange(s, e):
            if (s, e) in memory:
                return memory[(s, e)]

            if s >= len(nums) or e >= len(nums) or s > e:
                return 0

            if s == e - 1:
                memory[(s, e)] = max(nums[s], nums[e])
                return memory[(s, e)]

            memory[(s, e)] = max(nums[s] + robRange(s + 2, e), robRange(s + 1, e))
            return memory[(s, e)]

        return max(nums[0] + robRange(2, len(nums) - 2), robRange(1, len(nums) - 1))
