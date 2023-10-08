class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        result = [0] * n

        for i in range(n - 2, -1, -1):
            min_value = 100000
            for j in range(i + 1, min(n, i + nums[i] + 1)):
                min_value = min(min_value, result[j])

            result[i] = min_value + 1

        return result[0]
