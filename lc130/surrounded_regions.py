class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        safe = set()
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c):
            if (r, c) in safe or board[r][c] == "X":
                return

            safe.add((r, c))

            if r - 1 >= 0 and board[r - 1][c] == "O":
                dfs(r - 1, c)
            if r + 1 < ROWS and board[r + 1][c] == "O":
                dfs(r + 1, c)
            if c - 1 >= 0 and board[r][c - 1] == "O":
                dfs(r, c - 1)
            if c + 1 < COLS and board[r][c + 1] == "O":
                dfs(r, c + 1)

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)


        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                if (r, c) not in safe:
                    board[r][c] = "X"

