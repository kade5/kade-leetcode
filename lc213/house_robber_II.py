class Solution:
    def rob(self, nums: list[int]) -> int:
        def robRange(s, e):
            rob1, rob2 = 0, 0

            while s <= e:
                temp = max(nums[s] + rob1, rob2)
                rob1 = rob2
                rob2 = temp
                s += 1

            return rob2

        if len(nums) == 1:
            return nums[0]

        return max(robRange(0, len(nums) - 2), robRange(1, len(nums) - 1))
