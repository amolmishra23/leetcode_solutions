class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Navigate as deep from the borders, making the O as .
        Next iteration mark all the O as X
        And mark all the . as O
        Hence the problem is solved
        """
        def dfs(board, i, j):
            if 0<=i<len(board) and 0<=j<len(board[0]) and board[i][j]=='O':
                board[i][j] = '.'
                dfs(board, i-1, j)
                dfs(board, i+1, j)
                dfs(board, i, j-1)
                dfs(board, i, j+1)
                
    
        if not board or not board[0]: return 
            
        # navigating the first and low row, through DFS
        for i in [0, len(board)-1]:
            for j in range(len(board[0])):
                dfs(board, i, j)

        # navigating the first and last column, through DFS
        for i in range(len(board)):
            for j in [0, len(board[0])-1]:
                dfs(board, i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='.':
                    board[i][j]='O'
