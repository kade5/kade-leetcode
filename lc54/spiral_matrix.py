class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        result = []

        while l <= r and t <= b:
            for i in range(r - l + 1):
                result.append(matrix[t][l + i])
            for i in range(1, b - t + 1):
                result.append(matrix[t + i][r])

            if t != b:
                for i in range(1, r - l + 1):
                    result.append(matrix[b][r - i])

            if l != r:
                for i in range(1, b - t):
                    result.append(matrix[b - i][l])

            l, r, t, b = l + 1, r - 1, t + 1, b - 1

        return result


if __name__ == "__main__":
    result = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    s = Solution()
    new_result = s.spiralOrder(result)
