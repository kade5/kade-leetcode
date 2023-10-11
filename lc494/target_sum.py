from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        max_value = sum(nums)
        min_value = -max_value
        cache = defaultdict(int)

        cache[(0, nums[0])] += 1
        cache[(0, -nums[0])] += 1

        for i in range(1, n):
            num = nums[i]
            for t in range(min_value, max_value + 1):
                cache[(i, t)] = cache[(i - 1, t - num)] + cache[(i - 1, t + num)]

        return cache[(n - 1, target)]
