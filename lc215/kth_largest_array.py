class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        left = 0
        right = len(nums) - 1

        while True:
            val = right
            part = left
            for i in range(left, val):
                if nums[i] <= nums[val]:
                    swap = nums[part]
                    nums[part] = nums[i]
                    nums[i] = swap
                    part += 1

            swap = nums[val]
            nums[val] = nums[part]
            nums[part] = swap

            if part == len(nums) - k:
                return nums[part]
            elif len(nums) - k > part:
                left = part + 1
            else:
                right = part - 1
