import heapq
class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False
        hash_map = {}
        min_heap = []

        for card in hand:
            if card not in hash_map:
                hash_map[card] = 1
                heapq.heappush(min_heap, card)
            else:
                hash_map[card] += 1


        while min_heap:
            current_value = min_heap[0]
            if hash_map[current_value] == 0:
                heapq.heappop(min_heap)
                continue
            hash_map[current_value] -= 1

            for i in range(1, groupSize):
                if current_value + i not in hash_map or hash_map[current_value + i] == 0:
                    return False
                hash_map[current_value + i] -= 1

        return True
