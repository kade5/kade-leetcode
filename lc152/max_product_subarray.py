import math
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maximum = -math.inf
        prod_list = []

        for num in nums:
            for i in range(len(prod_list)):
                prod_list[i] = num * prod_list[i]
                if prod_list[i] > maximum:
                    maximum = prod_list[i]

            if num > maximum:
                maximum = num

            prod_list.append(num)


        return int(maximum)

