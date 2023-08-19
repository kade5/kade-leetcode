class Trie:
    def __init__(self):
        self.next = {}
        self.word = False


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        trie = self.buildTrie(wordDict)
        cache = {}

        def search(s):
            if s in cache:
                return cache[s]
            current_trie = trie
            i = 0
            found = False
            while i < len(s) and not found:
                if current_trie.word:
                    found = search(s[i:])
                if s[i] not in current_trie.next:
                    break
                current_trie = current_trie.next[s[i]]
                i += 1

            if i == len(s) and current_trie.word:
                cache[s] = True
                return True

            cache[s] = found
            return found

        return search(s)

    def buildTrie(self, wordDict):
        head = Trie()
        currentTrie = head

        for word in wordDict:
            currentTrie = head
            for letter in word:
                if letter in currentTrie.next:
                    currentTrie = currentTrie.next[letter]
                else:
                    currentTrie.next[letter] = Trie()
                    currentTrie = currentTrie.next[letter]

            currentTrie.word = True

        return head
