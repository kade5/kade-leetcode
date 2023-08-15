from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        queue = deque()
        visited = set()
        wordList.append(beginWord)
        graph = self.buildGraph(wordList)
        count = 1
        visited.add(beginWord)

        for stub in self.findWordStubs(beginWord):
            for adj in graph[stub]:
                if adj not in visited:
                    queue.append(adj)

        while queue:
            count += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return count
                for stub in self.findWordStubs(word):
                    for adj in graph[stub]:
                        if adj not in visited:
                            visited.add(adj)
                            queue.append(adj)

        return 0

    def findWordStubs(self, word):
        stubs = []
        for i in range(len(word)):
            stub = word[0:i] + "*" + word[i + 1 : len(word)]
            stubs.append(stub)

        return stubs

    def buildGraph(self, wordList):
        graph = {}
        for word in wordList:
            stubs = self.findWordStubs(word)
            for stub in stubs:
                if graph.get(stub):
                    graph[stub].append(word)
                else:
                    graph[stub] = [word]

        return graph
