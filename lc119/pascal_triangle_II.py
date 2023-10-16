class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        result = [1]

        for _ in range(1, rowIndex + 1):
            result.append(1)

            for i in range(len(result) - 2, 0, -1):
                result[i] = result[i] + result[i - 1]

        return result
