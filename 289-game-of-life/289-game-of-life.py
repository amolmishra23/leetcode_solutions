class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Around each cell, we need to count the live_count. Based on that apply rules. 
        """
        if board is None or len(board)==0 or len(board[0])==0: return board

        m, n = len(board), len(board[0])
        res = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                live_count = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx==dy==0: continue
                        x, y = i+dx, j+dy
                        if x>=0 and x<m and y>=0 and y<n and board[x][y]==1:
                            live_count += 1

                if board[i][j]==0 and live_count==3:
                    res[i][j]=1
                elif board[i][j]==1 and live_count in [2,3]:
                    res[i][j]=1
        
        for i in range(m):
            for j in range(n):
                board[i][j] = res[i][j]