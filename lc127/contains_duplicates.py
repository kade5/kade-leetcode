class Solution(object):
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dict = {}

        for num in nums:
            if nums_dict.get(num):
                return True
            else:
                nums_dict[num] = True

        return False
