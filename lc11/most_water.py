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

        for start in range(len(height) - 1):
            end = len(height) - 1
            x_length = end - start
            local_max = 0
            while start < end:
                if height[end] >= height[start]:
                    local_max = max(local_max, height[start] * x_length)
                    break
                else:
                    local_max = max(local_max, height[end] * x_length)
                    end -= 1
                    x_length -= 1
            max_height = max(max_height, local_max)

        return max_height
