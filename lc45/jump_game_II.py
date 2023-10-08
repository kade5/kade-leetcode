class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        result = 0
        l, r = 0, 0

        while r < n - 1:
            max_jump = 0
            for i in range(l, r + 1):
                max_jump = max(max_jump, nums[i] + i)

            result += 1
            l = r + 1
            r = max_jump

        return result
