class WordDict:
    def __init__(self):
        self.trie = {}
        self.word = False

    def addWord(self, word):
        current_trie = self.trie
        for c in word:
            if not current_trie.get(c):
                current_trie[c] = WordDict()
                current_trie = current_trie[c].trie
            else:
                current_trie = current_trie[c].trie
        self.word = True


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = self.makeDict(words)
        rows, cols = len(board), len(board[0])
        found_words, visited_pos = set(), set()

        def findWordsFromPos(r, c, board, word_dict, word):
            nonlocal rows
            nonlocal cols
            nonlocal visited_pos
            nonlocal found_words
            if (
                r < 0
                or c < 0
                or r == rows
                or c == cols
                or (r, c) in visited_pos
                or board[r][c] not in word_dict.trie
            ):
                return
            
            visited_pos.add((r, c))
            word_dict = word_dict.trie[board[r][c]]
            word += board[r][c]
            if word_dict.word:
                found_words.add(word)

            findWordsFromPos(r - 1, c, board, word_dict, word)
            findWordsFromPos(r + 1, c, board, word_dict, word)
            findWordsFromPos(r, c - 1, board, word_dict, word)
            findWordsFromPos(r, c + 1, board, word_dict, word)

            visited_pos.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                findWordsFromPos(r, c, board, root, "")

        return list(found_words)

    def makeDict(self, words: list[str]) -> WordDict:
        head = WordDict()
        for word in words:
            head.addWord(word)
        return head
