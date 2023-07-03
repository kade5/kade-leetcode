class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Given n non-negative integers representing an elevation map where
        the width of each bar is 1, compute how much water it can trap after
        raining.
        :type height: List[int]
        :rtype: int
        """

        sum_water = 0
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]

        while left < right:
            if left_max > right_max:
                right -= 1
                right_max = max(right_max, height[right])
                sum_water += right_max - height[right]
            else:
                left += 1
                left_max = max(left_max, height[left])
                sum_water += left_max - height[left]

        return sum_water
