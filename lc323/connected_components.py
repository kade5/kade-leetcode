class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]
        result_set = set()

        def findParent(i):
            p = parent[i]

            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(a, b):
            pa, pb = findParent(a), findParent(b)

            if pa == pb:
                return
            if rank[pa] > rank[pb]:
                rank[pa] += rank[pb]
                parent[pb] = pa
            else:
                rank[pb] += rank[pa]
                parent[pa] = pb

        for pair in edges:
            union(pair[0], pair[1])

        for i in parent:
            result_set.add(findParent(i))

        return len(result_set)
