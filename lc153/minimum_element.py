class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Given the sorted rotated array nums of unique elements,
        return the minimum element of this array.
                :type nums: List[int]
                :rtype: int
        """
        len_nums = len(nums)
        left = 0
        right = len_nums - 1
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= nums[(mid - 1) % len_nums]:
                break
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return nums[mid]
