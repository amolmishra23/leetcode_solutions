class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows, num_cols, n = len(board), len(board[0]), len(word)
        
        def solve(r, c, idx):
            if idx == n: return True
            
            if 0<=r<num_rows and 0<=c<num_cols and board[r][c]==word[idx]:
                char = board[r][c]
                board[r][c] = ""
                
                for rr, cc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    if solve(rr, cc, idx+1): return True
                
                board[r][c] = char
        
        for i in range(num_rows):
            for j in range(num_cols):
                if solve(i, j, 0): return True
            
        return False