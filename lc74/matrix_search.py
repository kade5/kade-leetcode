class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Given an integer target and sorted matrix, return true if target
        is in matrix or false otherwise.
                :type matrix: List[List[int]]
                :type target: int
                :rtype: bool
        """
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        row_index = 0
        col_index = 0

        while top <= bottom:
            row_index = (top + bottom) // 2
            if matrix[row_index][left] <= target <= matrix[row_index][right]:
                break
            elif target < matrix[row_index][left]:
                bottom = row_index - 1
            else:
                top = row_index + 1

        while left <= right:
            col_index = (left + right) // 2
            if target == matrix[row_index][col_index]:
                return True
            elif target < matrix[row_index][col_index]:
                right = col_index - 1
            else:
                left = col_index + 1
        return False
