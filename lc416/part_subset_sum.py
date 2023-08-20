class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False
        sum_nums = sum_nums // 2

        if nums[len(nums) - 1] == sum_nums:
            return True

        cache = [set()] * len(nums)
        cache[len(nums) - 1].add(nums[len(nums) - 1])

        for i in range(len(nums) - 2, -1, -1):
            new_set = set()
            if nums[i] == sum_nums:
                return True
            for s in cache[i + 1]:
                if nums[i] + s == sum_nums:
                    return True
                if nums[i] + s < sum_nums:
                    new_set.add(nums[i] + s)
            if nums[i] < sum_nums:
                cache[i].add(nums[i])
            cache[i + 1].update(new_set)

        return False
