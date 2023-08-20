class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False
        sum_nums = sum_nums // 2

        if nums[len(nums) - 1] == sum_nums:
            return True

        cache = [[]] * len(nums)
        cache[len(nums) - 1].append(nums[len(nums) - 1])

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == sum_nums:
                return True
            for s in range(len(cache[i + 1])):
                cur_sum = cache[i + 1][s]
                if nums[i] + cur_sum == sum_nums:
                    return True
                if nums[i] + cur_sum < sum_nums:
                    cache[i].append(nums[i] + cur_sum)
            if nums[i] < sum_nums:
                cache[i].append(nums[i])

        return False
