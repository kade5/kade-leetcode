class Solution(object):
    def maxArea(self, height: list[int]) -> int:
        """
        You are given an integer array height of length n. There are
        n vertical lines drawn such that the two endpoints of the ith
        line are (i, 0) and (i, height[i]).

        Find two lines that together with the x-axis form a container,
        such that the container contains the most water.

        Return the maximum amount of water a container can store.
                :type height: List[int]
                :rtype: int
        """
        max_height = 0

        start = 0
        end = len(height) - 1

        while start < end:
            max_height = max(
                max_height, min(height[start], height[end]) * (end - start)
            )

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_height
