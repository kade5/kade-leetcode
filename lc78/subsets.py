class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        power_set = [[]]
        
        for num in nums:
            for i in range(len(power_set)):
                new_subset = power_set[i].copy()
                new_subset.append(num)
                power_set.append(new_subset)
        return power_set
