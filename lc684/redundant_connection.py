class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent = [node for node in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def findParent(n):
            p = parent[n]

            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(n1, n2):
            p1, p2 = findParent(n1), findParent(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True

        for pair in edges:
            if not union(pair[0], pair[1]):
                return pair

        return []
