class Solution:
    def alienOrder(self, words: list[str]) -> str:
        tree = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_length = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_length] == w2[:min_length]:
                return ""

            for j in range(min_length):
                if w1[j] != w2[j]:
                    tree[w1[j]].add(w2[j])
                    break

        visit = {}
        result = []

        def dfs(c):
            if c in visit:
                return visit[c]

            visit[c] = True

            for adj in tree[c]:
                if dfs(adj):
                    return True

            visit[c] = False
            result.append(c)

        for c in tree:
            if dfs(c):
                return ""

        result.reverse()
        return "".join(result)
