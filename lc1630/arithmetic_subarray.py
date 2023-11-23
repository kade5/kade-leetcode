class Solution:
    def checkArithmeticSubarrays(
        self, nums: list[int], l: list[int], r: list[int]
    ) -> list[bool]:
        result = []

        def checkSubarray(nums, b, e):
            sub = nums[b : e + 1]
            sub.sort()
            sum = sub[1] - sub[0]

            for i in range(1, len(sub) - 1):
                if sub[i + 1] - sub[i] != sum:
                    return False

            return True

        for i in range(len(l)):
            result.append(checkSubarray(nums, l[i], r[i]))

        return result
