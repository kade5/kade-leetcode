class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()

        def checkSum(i, subset):
            if i == len(candidates):
                return
            subset.append(candidates[i])
            if sum(subset) == target:
                result.append(subset.copy())
            elif sum(subset) < target:
                checkSum(i + 1, subset)

            subset.pop()

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            checkSum(i + 1, subset)

        checkSum(0, [])
        return result

