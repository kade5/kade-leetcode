class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Given the array nums after the possible rotation and an integer
        target, return the index of target if it is in nums, or -1 if it
        is not in nums.
                        :type nums: List[int]
                        :type target: int
                        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if nums[mid] < nums[left] and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] > nums[right] and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
