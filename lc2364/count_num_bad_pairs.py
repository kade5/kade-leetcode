class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        count_bad = 0

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                i_diff = j - i
                num_diff = nums[j] - nums[i]
                if i_diff != num_diff:
                    count_bad += 1

        return count_bad
