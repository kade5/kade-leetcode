class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        def findWord(i, j, current_word, pos_set) -> bool:
            current_word = current_word + board[i][j]
            if current_word == word:
                return True
            if (i, j) in pos_set:
                return False
            
            if i > 0:
                pos_set.add((i, j))
                findWord(i - 1, j, current_word, pos_set)
                pos_set.remove((i, j))
            if i < len(board) - 1:
                pos_set.add((i, j))
                findWord(i + 1, j, current_word, pos_set)
                pos_set.remove((i, j))
            if j > 0:
                pos_set.add((i, j))
                findWord(i, j - 1, current_word, pos_set)
                pos_set.remove((i, j))
            if j < len(board[0]) - 1:
                pos_set.add((i, j))
                findWord(i, j + 1, current_word, pos_set)
                pos_set.remove((i, j))
            return False
        
        for m in range(len(board)):
            for n in range(len(board[0])):
                if findWord(m, n, "", set()):
                    return True
        return False

