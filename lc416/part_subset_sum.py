class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False
        sum_nums = sum_nums // 2

        cache = set()
        cache.add(0)

        for i in range(len(nums) - 1, -1, -1):
            new_set = set()
            for s in cache:
                if nums[i] + s == sum_nums:
                    return True
                if nums[i] + s < sum_nums:
                    new_set.add(nums[i] + s)
            cache.update(new_set)

        return False
