class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        Given an array of integers heights representing the histogram's
        bar height where the width of each bar is 1, return the area of
        the largest rectangle in the histogram.
                :type heights: List[int]
                :rtype: int
        """
        max_height = 0
        stack = []

        for index, h in enumerate(heights):
            start = index
            while stack and h < stack[-1][1]:
                prev_index, prev_height = stack.pop()
                max_height = max(max_height, prev_height * (index - prev_index))
                start = prev_index
            stack.append((start, h))

        for index, h in stack:
            max_height = max(max_height, h * (len(heights) - index))
        return max_height
