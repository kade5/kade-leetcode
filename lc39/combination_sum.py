class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()

        def checkSum(check_list, candidates):
            for i in range(len(candidates)):
                check_list.append(candidates[i])
                if sum(check_list) == target:
                    result.append(check_list)
                    break
                elif sum(check_list) > target:
                    break
                else:
                    checkSum(check_list.copy(), candidates[i:])
                check_list.pop()

        check_list = []
        checkSum(check_list, candidates)
        return result
