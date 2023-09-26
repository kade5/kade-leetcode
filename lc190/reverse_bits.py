class Solution:
    def reverseBits(self, n: int) -> int:
        bits = 32
        result = 0

        for i in range(bits):
            if n & (2**i):
                result = result + (2 ** (bits - 1 - i))

        return result
