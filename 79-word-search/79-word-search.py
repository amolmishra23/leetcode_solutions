class Solution:
    def solve(self, i, j, curr=0):
        if curr == len(self.word): return True
            
        if 0<=i<self.m and 0<=j<self.n and self.board[i][j]==self.word[curr]:
            temp = self.board[i][j]
            self.board[i][j] = ""
            
            for r, c in [(i-1, j), (i+1, j), (i, j-1), (i,j+1)]:
                if self.solve(r, c, curr+1): return True
            
            self.board[i][j] = temp
                
        return False
        
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        self.m, self.n = len(board), len(board[0])
        self.board, self.word = board, word
        
        for i in range(self.m):
            for j in range(self.n):
                if self.solve(i, j): return True
                
        return False