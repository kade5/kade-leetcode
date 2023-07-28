class Trie:
    def __init__(self):
        self.letter_map = {}

    def insert(self, word: str) -> None:
        current_trie = self.letter_map
        if word:
            word = word + "*"
        for c in word:
            if not current_trie.get(c):
                current_trie[c] = Trie()
                current_trie = current_trie[c].letter_map
            else:
                current_trie = current_trie[c].letter_map

    def search(self, word: str) -> bool:
        if word:
            word = word + "*"
        return self.startsWith(word)

    def startsWith(self, prefix: str) -> bool:
        current_trie = self.letter_map
        for c in prefix:
            if not current_trie.get(c):
                return False
            else:
                current_trie = current_trie[c].letter_map
        return True
