class Solution:
    def getSum(self, a: int, b: int) -> int:
        result = abs(a)
        remain = abs(b)

        if result < remain:
            return self.getSum(b, a)

        sign = 1 if a > 0 else -1

        if a * b >= 0:
            while remain != 0:
                temp = result ^ remain
                remain = (result & remain) << 1
                result = temp

        else:
            while remain != 0:
                temp = result ^ remain
                remain = ((~result) & remain) << 1
                result = temp

        return result * sign
