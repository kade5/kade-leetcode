class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [nums[0]]

        for i in range(1, n):
            prefix.append(prefix[-1] + nums[i])

        result = []

        for i in range(n):
            left_sum = prefix[i] - nums[i]
            right_sum = prefix[-1] - prefix[i]

            right_count = n - 1 - i

            left_total = i * nums[i] - left_sum
            right_total = right_sum - right_count * nums[i]

            result.append(left_total + right_total)

        return result
