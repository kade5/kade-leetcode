class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        def findWord(i, j, current_word, pos_set, found) -> bool:
            if (i, j) in pos_set:
                return found
            current_word = current_word + board[i][j]
            if current_word == word:
                return True
            
            if i > 0 and not found:
                pos_set.add((i, j))
                found = findWord(i - 1, j, current_word, pos_set, found)
                pos_set.remove((i, j))
            if i < len(board) - 1 and not found:
                pos_set.add((i, j))
                found = findWord(i + 1, j, current_word, pos_set, found)
                pos_set.remove((i, j))
            if j > 0 and not found:
                pos_set.add((i, j))
                found = findWord(i, j - 1, current_word, pos_set, found)
                pos_set.remove((i, j))
            if j < len(board[0]) - 1 and not found:
                pos_set.add((i, j))
                found = findWord(i, j + 1, current_word, pos_set, found)
                pos_set.remove((i, j))
            return found
        
        for m in range(len(board)):
            for n in range(len(board[0])):
                if findWord(m, n, "", set(), False):
                    return True
        return False

