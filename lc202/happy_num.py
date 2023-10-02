class Solution:
    def isHappy(self, n: int) -> bool:
        num_set = set([n])

        def reduce(n: int) -> int:
            result = 0
            while n != 0:
                result += (n % 10) ** 2
                n = n // 10

            return result

        while n != 1:
            n = reduce(n)
            if n in num_set:
                return False
            num_set.add(n)

        return True
