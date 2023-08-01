class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def findWord(i, j, current_word, pos_set, found) -> bool:
            if (
                i < 0
                or j < 0
                or i >= len(board)
                or j >= len(board[0])
                or (i, j) in pos_set
                or (len(current_word) > 0 and board[i][j] != current_word[0])
            ):
                return found
            if current_word == board[i][j]:
                return True
            pos_set.add((i, j))
            if not found:
                found = findWord(i - 1, j, current_word[1:], pos_set, found)
            if not found:
                found = findWord(i + 1, j, current_word[1:], pos_set, found)
            if not found:
                found = findWord(i, j - 1, current_word[1:], pos_set, found)
            if not found:
                found = findWord(i, j + 1, current_word[1:], pos_set, found)
            pos_set.remove((i, j))
            return found

        for m in range(len(board)):
            for n in range(len(board[0])):
                if findWord(m, n, word, set(), False):
                    return True
        return False
