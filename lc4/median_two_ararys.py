import math


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Given two sorted arrays nums1 and nums2 of size m and n respectively,
        return the median of the two sorted arrays.
                :type nums1: List[int]
                :type nums2: List[int]
                :rtype: float
        """
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums1) <= len(nums2):
            smaller, larger = nums1, nums2
        else:
            smaller, larger = nums2, nums1

        left = 0
        right = len(smaller) - 1

        while True:
            mid1 = (left + right) // 2
            mid2 = half - mid1 - 2

            part1 = smaller[mid1] if mid1 >= 0 else -math.inf
            part1_next = smaller[mid1 + 1] if mid1 + 1 < len(smaller) else math.inf
            part2 = larger[mid2] if mid2 >= 0 else -math.inf
            part2_next = larger[mid2 + 1] if mid2 + 1 < len(larger) else math.inf

            if part1 <= part2_next and part2 <= part1_next:
                break

            if part1 > part2_next:
                right = mid1 - 1
            else:
                left = mid1 + 1

        if total % 2 == 0:
            return (max(part1, part2) + min(part1_next, part2_next)) / 2
        return min(part1_next, part2_next)
