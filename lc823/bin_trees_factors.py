from collections import defaultdict


class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        modulo = 10**9 + 7
        arr.sort()
        cache = defaultdict(int)
        numset = set(arr)
        sum = 0

        for i in range(len(arr)):
            current = arr[i]
            cache[current] += 1

            for j in range(0, i):
                check = arr[j]
                multiple = current // check

                if current % check == 0 and multiple in numset:
                    cache[current] += cache[check] * cache[multiple]
                    cache[current] %= modulo

            sum = (sum + cache[current]) % modulo

        return sum
