class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        current_trie = self.trie
        if word:
            word = word + '*'
        for c in word:
            if not current_trie.get(c):
                current_trie[c] = WordDictionary()
                current_trie = current_trie[c].trie
            else:
                current_trie = current_trie[c].trie

        

    def search(self, word: str) -> bool:
        current_trie = self.trie

        for i in range(len(word)):
            if word[i] == '.':
                for c in current_trie.keys():
                    if current_trie[c].search(word[i+1:]):
                        return True
                return False
            elif not current_trie.get(word[i]):
                return False
            else:
                current_trie = current_trie[word[i]].trie
        if current_trie.get('*'):
            return True
        return False
