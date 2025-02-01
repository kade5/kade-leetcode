class SparseVector:
    def __init__(self, nums: list[int]):
        self._nums = {}
        for i, num in enumerate(nums):
            if num != 0:
                self._nums[i] = num


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0
        for k, v in self._nums.items():
            product += v * vec._nums.get(k, 0)

        return product
