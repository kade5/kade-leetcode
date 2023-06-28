class Solution(object):
    def threeSum(self, nums: list[int]):
        """
        Given an integer array nums, return all the triplets
        [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
        and nums[i] + nums[j] + nums[k] == 0.
                :type nums: List[int]
                :rtype: List[List[int]]
        """
        results = []
        nums.sort()

        for index, value in enumerate(nums):
            if value > 0:
                break
            start = index + 1
            end = len(nums) - 1
            while start < end:
                if value + nums[start] + nums[end] == 0:
                    results.append([nums[index], nums[start], nums[end]])
                    break
                elif value + nums[start] + nums[end] > 0:
                    end -= 1
                else:
                    start += 1
        return results
