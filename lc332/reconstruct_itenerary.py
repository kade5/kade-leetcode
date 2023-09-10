class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        result = ["JFK"]
        tickets.sort()
        tree = self.buildGraph(tickets)

        def dfs(cur):
            if len(result) == len(tickets) + 1:
                return True
            if cur not in tree:
                return False

            temp = list(tree[cur])
            for i, v in enumerate(temp):
                tree[cur].pop(i)
                result.append(v)

                if dfs(v):
                    return True

                tree[cur].insert(i, v)
                result.pop()

            return False

        dfs("JFK")
        return result

    def buildGraph(self, tickets):
        tree = {}
        for beg, dest in tickets:
            if beg in tree:
                tree[beg].append(dest)
            else:
                tree[beg] = [dest]

        return tree
