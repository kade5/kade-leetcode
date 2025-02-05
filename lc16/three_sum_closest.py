import math



class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        difference = math.inf
        ans = 10000
        nums.sort()

        for l, num in enumerate(nums):
            r = len(nums) - 1
            mid = l + 1

            while mid < r:
                three_sum = nums[l] + nums[mid] + nums[r]
                if three_sum == target:
                    return three_sum
                new_difference = target - three_sum
                if abs(new_difference) < abs(difference):
                    difference = new_difference
                    ans = three_sum

                if three_sum > target:
                    r -= 1
                else:
                    mid += 1

        return ans