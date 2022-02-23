class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Start from the boundary, and use DFS (or BFS) to flip the 'O's that are connected to the edge to a third symbol (e.g., "Z")
        Scan the matrix again to flip the remaining 'O' to 'X', and the third symbol back to 'O'
        
        Navigate as deep from the borders, making the O as .
        Next iteration mark all the O as X
        And mark all the . as O
        Hence the problem is solved
        Concept is to go as deep as possible. from the boundaries
          marking the existing 0 as . 
          Because they cant be convered as X, for not being covered by island on all 4 sides.
        """
        def dfs(board, i, j):
            if 0<=i<len(board) and 0<=j<len(board[0]) and board[i][j]=='O':
                board[i][j] = '.'
                dfs(board, i-1, j)
                dfs(board, i+1, j)
                dfs(board, i, j-1)
                dfs(board, i, j+1)
                
        if not board or not board[0]: return
        m, n = len(board), len(board[0])
        
        for i in [0, m-1]:
            for j in range(n):
                dfs(board, i, j)
                
        for i in range(m):
            for j in [0, n-1]:
                dfs(board, i, j)
                
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O': board[i][j] = 'X'
                elif board[i][j]=='.': board[i][j]='O'