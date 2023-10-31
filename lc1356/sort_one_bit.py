class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        def find_one_bits(nums: int) -> int:
            ones = 1
            result = 0

            while nums:
                if nums & ones:
                    result += 1
                    nums ^= ones

                ones <<= 1

            return result

        arr.sort(key=lambda x: (find_one_bits(x), x))
        return arr
