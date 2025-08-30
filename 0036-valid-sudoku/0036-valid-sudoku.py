class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def is_valid_row(row):
            elem = [x for x in row if x!="."]
            return len(elem) == len(set(elem))

        for i in range(9):
            if not is_valid_row([board[i][j] for j in range(9)]) or \
                not is_valid_row([board[j][i] for j in range(9)]):
                return False

        for i in range(3):
            for j in range(3):
                if not is_valid_row(board[m][n] for m in range(3*i, 3*i+3) for n in range(3*j, 3*j+3)):
                    return False

        return True