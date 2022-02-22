class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        digits = set('123456789')
        # to keep track of all unfilled blocks.
        # the moment we fill all the blocks, means its a valid combination and can return true. 
        not_visited = deque([(i,j) for i in range(9) for j in range(9) if board[i][j]=="."])
        
        def valid_choices(board, i, j):
            """
            For row, col its simple only
            for (5,0) lets say, the grid is from 
            3,0 3,1 3,2
            4,0 4,1 4,2
            5,0 5,1 5,2
            
            5//3 = 1 # this is to find which block it falls under. 
            5//3*3 = 3 # this is to start from starting of block. 
            
            Means it basically starts at (3,0)
            """
            row = board[i]
            col = [board[m][j] for m in range(9)]
            grid = [board[m][n] for m in range(i//3*3, i//3*3+3) for n in range(j//3*3, j//3*3+3)]
            
            choices = digits.difference(row).difference(col).difference(grid)
            
            return choices
        
        def solve(board, not_visited):
            if not not_visited: return True
            
            r, c = not_visited.popleft()
            
            for choice in valid_choices(board, r, c):
                board[r][c] = choice
                # if we encountered a valid combination, we would have retuned by now. 
                if solve(board, not_visited): return True
                board[r][c] = "."
                
            not_visited.appendleft((r, c))
            return False
        
        solve(board, not_visited)