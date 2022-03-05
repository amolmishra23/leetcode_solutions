class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        r, c = None,None
        dirs = [
            (0, 1), 
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        
        for i in range(8):
            for j in range(8):
                if board[i][j]=='R': r, c = i, j; break
        
        res = 0
        for x, y in dirs:
            nr, nc = r+x, c+y
            
            while 0<=nr<8 and 0<=nc<8:
                if board[nr][nc]=='p': res+=1
                if board[nr][nc]!='.': break
                nr, nc = nr+x, nc+y
        
        return res
                    