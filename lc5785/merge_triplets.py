class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        result = [False, False, False]
        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue
            for i in range(len(target)):
                if target[i] == trip[i]:
                    result[i] = True

        return result[0] and result[1] and result[2]
        
