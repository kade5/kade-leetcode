class Solution(object):
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        Determines if a 9 x 9 Sudoku board is valid.
                :type board: List[List[str]]
                :rtype: bool
        """
        column_dict = {}
        row_dict = {}
        block_dict = {}

        for i in range(len(board)):
            for j in range(len(board)):
                value = board[i][j]
                if value != ".":
                    if column_dict.get(j):
                        if column_dict.get(j, {}).get(value):
                            return False
                    column_dict[j] = self.update_dict(column_dict, j, value)
                    if row_dict.get(i):
                        if row_dict.get(i, {}).get(value):
                            return False
                    row_dict[i] = self.update_dict(row_dict, i, value)

                    block_tuple = self.get_block_tuple(i, j)
                    if block_dict.get(block_tuple):
                        if block_dict.get(block_tuple, {}).get(value):
                            return False
                    block_dict[block_tuple] = self.update_dict(
                        block_dict, block_tuple, value
                    )

        return True

    def get_block_tuple(self, i, j):
        return int(i / 3.0) * 3 + int(j / 3.0)

    def update_dict(self, a_dict, pos, value):
        temp_dict = a_dict.get(pos, {})
        temp_dict.update({value: True})
        return temp_dict
