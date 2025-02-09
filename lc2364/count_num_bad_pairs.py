from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        n = len(nums)
        count_bad = n * (n - 1) // 2
        num_hash = defaultdict(int)

        for i, num in enumerate(nums):
            num_hash[num - i] += 1

        for key, value in num_hash.items():
            if value > 1:
                count_bad -= value * (value - 1) // 2

        return count_bad

