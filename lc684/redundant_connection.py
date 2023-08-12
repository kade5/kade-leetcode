class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        trees = [{node} for node in range(1, len(edges) + 1)]

        for pair in edges:
            temp_set = set()
            for i in range(len(trees)):
                if pair[0] in trees[i] and pair[1] in trees[i]:
                    return pair
                if not temp_set and (pair[0] in trees[i] or pair[1] in trees[i]):
                    temp_set = trees[i]
                    trees[i] = set()
                elif pair[1] in trees[i] or pair[0] in trees[i]:
                    trees[i] = trees[i].union(temp_set)

        return []
