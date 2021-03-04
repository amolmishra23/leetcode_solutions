class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        digits = set('123456789')
        not_visited = deque([(r,c) for r in range(9) for c in range(9) if board[r][c]=="."])
        
        def valid_choices(board, i, j):
            row = board[i]
            col = [board[m][j] for m in range(9)]
            grid = [board[m][n] for m in range(i//3*3, i//3*3+3)
                                for n in range(j//3*3, j//3*3+3)]
            choices = digits.difference(row).difference(col).difference(grid)
            return choices
        
        def solve(board, not_visited):
            if not not_visited: return True
            r, c = not_visited.popleft()
            
            for digit in valid_choices(board, r, c):
                board[r][c] = digit
                if solve(board, not_visited): return True
                board[r][c] = "."
            
            not_visited.appendleft((r,c))
            False
            
        solve(board, not_visited)