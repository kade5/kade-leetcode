class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        consec_ones = [[0] * n for _ in range(m)]

        for j in range(n):
            ones = 0
            for i in range(m):
                if matrix[i][j] == 1:
                    ones += 1
                else:
                    ones = 0
                consec_ones[i][j] = ones

        max_area = 0

        for row in consec_ones:
            row.sort(reverse=True)
            max_row = 0
            for i, element in enumerate(row):
                if element == 0:
                    break

                cur_row = (i + 1) * element
                max_row = max(cur_row, max_row)

            max_area = max(max_row, max_area)

        return max_area
