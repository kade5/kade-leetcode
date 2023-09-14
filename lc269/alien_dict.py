from collections import deque


class Solution:
    def alienOrder(self, words: list[str]) -> str:
        letters = set()
        prev_word = words[0]
        result = ""
        queue = deque()
        for word in words:
            for letter in word:
                letters.add(letter)

        queue.append(prev_word[0])

        graph = {l: [] for l in letters}

        for word in words[1:]:
            i = 0
            while i < len(word) and word[i] == prev_word[i]:
                i += 1

            if i < len(word):
                graph[word[i]].append(prev_word[i])

        letters = list(letters)

        for letter in letters:
            queue.append(letter)

            while queue:
                cur = queue.popleft()
                if cur in result:
                    return ""

                result += cur
                letters.remove(cur)

                for adj in graph[cur]:
                    queue.append(adj)

        return result
