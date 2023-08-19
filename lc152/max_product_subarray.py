class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maximum = nums[0]
        cur_max = 1
        cur_min = 1

        for num in nums:
            temp = cur_max * num
            cur_max = max(temp, num * cur_min, num)
            cur_min = min(temp, num * cur_min, num)
            maximum = max(maximum, cur_max)

        return maximum
