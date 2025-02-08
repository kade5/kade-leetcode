import heapq


class Solution:
    def makePrefSumNonNegative(self, nums: list[int]) -> int:
        prefix_sum = 0
        min_heap = []
        operations = 0

        for i, _ in enumerate(nums):
            heapq.heappush(min_heap, (nums[i], i))
            prefix_sum += nums[i]
            if prefix_sum < 0:
                val, min_index = heapq.heappop(min_heap)
                operations += 1
                prefix_sum -= val

        return operations
