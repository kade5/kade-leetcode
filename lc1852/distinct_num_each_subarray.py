from collections import defaultdict


class Solution:
    def distinctNumbers(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        ans = [0] * (n - k + 1)
        distinct_dict = defaultdict(int)
        for i in range(k):
            distinct_dict[nums[i]] += 1

        ans[0] = len(distinct_dict)
        start_pos = 1
        end_pos = k

        while end_pos < n:
            ans[start_pos] = ans[start_pos - 1]
            distinct_dict[nums[start_pos - 1]] -= 1
            if distinct_dict[nums[start_pos - 1]] == 0:
                ans[start_pos] -= 1
            distinct_dict[nums[end_pos]] += 1
            if distinct_dict[nums[end_pos]] == 1:
                ans[start_pos] += 1
            start_pos += 1
            end_pos += 1

        return ans