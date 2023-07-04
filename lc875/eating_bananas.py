from math import ceil


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """
        Koko loves to eat bananas. There are n piles of bananas, the ith
        pile has piles[i] bananas. The guards have gone and will come back
        in h hours. Koko can decide her bananas-per-hour eating speed of k.
        Each hour, she chooses some pile of bananas and eats k bananas from
        that pile. If the pile has less than k bananas, she eats all of
        them instead and will not eat any more bananas during this hour.

        Koko likes to eat slowly but still wants to finish eating all the
        bananas before the guards return.

        Return the minimum integer k such that she can eat all the bananas
        within h hours.
                :type piles: List[int]
                :type h: int
                :rtype: int
        """
        hpp = h // len(piles)
        min_range = ceil(min(piles) / hpp)
        max_range = ceil(max(piles) / hpp)
        mid = 0
        mid_value = 0

        while min_range <= max_range:
            mid = (max_range + min_range) // 2
            mid_value = self.calculate_mid(piles, mid)
            if mid_value == h:
                break
            elif mid_value > h:
                min_range = mid + 1
            else:
                max_range = mid - 1

        while mid > 0:
            mid_value = self.calculate_mid(piles, mid - 1)
            if mid_value != h:
                break
            mid -= 1

        return mid

    def calculate_mid(self, piles, mid):
        hours = 0
        for bananas in piles:
            hours += ceil(bananas / mid)
        return hours
