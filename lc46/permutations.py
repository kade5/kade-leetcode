class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def permutation(nums, current_perm):
            if not nums:
                result.append(current_perm)
                return
            for i in range(len(nums)):
                current_perm.append(nums[i])
                new_nums = nums.copy()
                new_nums.pop(i)
                permutation(new_nums, current_perm.copy())
                current_perm.pop()

        permutation(nums, [])
        return result
