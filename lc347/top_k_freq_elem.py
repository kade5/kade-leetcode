class Solution(object):
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Given an integer array nums and an integer k, return the k most
        frequent elements. You may return the answer in any order.
                :type nums: List[int]
                :type k: int
                :rtype: List[int]
        """
        num_freq = {}

        for num in nums:
            num_freq[num] = 1 + num_freq.get(num, 0)

        sorted_nums = sorted(num_freq.items(), key=lambda x: x[1],
                             reverse=True)
        return [x[0] for x in sorted_nums[:k]]
