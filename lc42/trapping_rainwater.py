class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Given n non-negative integers representing an elevation map where
        the width of each bar is 1, compute how much water it can trap after
        raining.
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        current_max = 0
        current_max_index = 0
        total_rainwater = [0] * len(height)

        while left < len(height) - 1:
            current_max = -1
            current_max_index = 0
            right = left + 1
            total_rainwater[left] = 0
            if height[left] == 0:
                left += 1
                continue
            while right < len(height):
                if height[right] >= height[left]:
                    current_max = -1
                    left = right
                    break
                if height[right] > current_max:
                    current_max = height[right]
                    current_max_index = right
                total_rainwater[right] = height[left] - height[right]
                right += 1
            if current_max != -1:
                for index in range(left + 1, right):
                    total_rainwater[index] = current_max - height[index]
                left = current_max_index

        total_rainwater[-1] = 0
        return sum(total_rainwater)
