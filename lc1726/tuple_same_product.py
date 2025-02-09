from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        product_dict = defaultdict(list)

        i = 0
        j = 1
        tuple_count = 0

        while j < len(nums):
            while j < len(nums):
                num1, num2 = nums[i], nums[j]
                product_dict[num1 * num2].append((num1, num2))
                j += 1
            i += 1
            j = i + 1

        for product, tuples in product_dict.items():
            n = len(tuples)
            if n > 1:
                tuple_count += n * (n - 1) * 4

        return tuple_count
