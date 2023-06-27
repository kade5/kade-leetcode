class Solution(object):
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        Given an unsorted array of integers nums,
        return the length of the longest consecutive elements sequence.
                :type nums: List[int]
                :rtype: int
        """
        num_dict = {}
        longest_seq = 0

        for num in nums:
            num_dict[num] = True

        for num in num_dict.keys():
            if not num_dict.get(num - 1):
                current_seq_length = 1
                while num_dict.get(num + current_seq_length):
                    current_seq_length += 1

                longest_seq = max(longest_seq, current_seq_length)

        return longest_seq
