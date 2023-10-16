class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]

        current = [1, 1]

        for _ in range(1, rowIndex):
            prev = current.copy()
            current = [1]
            for j in range(1, len(prev)):
                current.append(prev[j - 1] + prev[j])

            current.append(1)

        return current
