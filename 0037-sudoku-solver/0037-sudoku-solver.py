class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        digits = set('123456789')
        not_visited = deque([(i,j) for i in range(9) for j in range(9) if board[i][j]=="."])

        def valid_choices(board, i, j):
            row = board[i]
            col = [board[m][j] for m in range(9)]
            grid = [board[m][n] for m in range(i//3*3, i//3*3+3) for n in range(j//3*3, j//3*3+3)]
            return digits.difference(row).difference(col).difference(grid)

        def solve(board, not_visited):
            if not not_visited: return True

            # Pick the cell with the fewest valid choices
            r, c = min(not_visited, key=lambda x: len(valid_choices(board, x[0], x[1])))
            not_visited.remove((r, c))

            for choice in valid_choices(board, r, c):
                board[r][c] = choice
                if solve(board, not_visited): return True
                board[r][c] = "."

            not_visited.append((r, c))
            return False

        solve(board, not_visited)